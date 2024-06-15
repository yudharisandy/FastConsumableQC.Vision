import numpy as np
import pickle
from functools import partial
from skimage import feature, future, segmentation
from sklearn.ensemble import RandomForestClassifier
from Common.VisionCommon import VisionCommon
from LowLevelAnalyzer.CircleChecker import CircleChecker
import logging
from Common.Label import Label
from LowLevelProcessor.BoundaryProcessor import BoundaryProcessor

class TipQCDetector:
    def __init__(self, isTrainTipQC):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(f"Object: {TipQCDetector.__name__} was created")
        
        self.visionCommon = VisionCommon()
        self.circleChecker = CircleChecker()
        self.boundaryProcessor = BoundaryProcessor()
        
        if(isTrainTipQC):
            self.classifier = RandomForestClassifier()
        else:
            with open('models/model.pkl', 'rb') as file:
                self.classifier = pickle.load(file)
        
        sigma_min = 1
        sigma_max = 16
        self.features_func = partial(
            feature.multiscale_basic_features,
            intensity=True,
            edges=True,
            texture=True,
            sigma_min=sigma_min,
            sigma_max=sigma_max,
            channel_axis=-1,
        )
        

    def Train(self, imageToTrain):
        self.logger.debug(f"Object: {TipQCDetector.__name__}, method: {TipQCDetector.Train.__name__}, start")

        height, width = imageToTrain.shape[:2]

        training_labels = np.zeros((height, width), dtype=np.uint8)
        training_labels[150:220, 140:210] = 1 # black background
        training_labels[20:90, 120:220] = 2 # tip body
        training_labels[270:340, 125:220] = 2 # tip body
        training_labels[130:230, 270:330] = 2 # tip body
        training_labels[130:250, 30:90] = 2 # tip body
        training_labels[155:215, 238:255] = 3 # plunger (white section)
        training_labels[120:140, 210:230] = 3 # plunger (white section)
        
        first_img_features = self.features_func(imageToTrain)
        self.classifier = future.fit_segmenter(training_labels, first_img_features, self.classifier)
        
        model_filename = 'models/model.pkl'
        
        self.logger.debug(f"Object: {TipQCDetector.__name__}, method: {TipQCDetector.Train.__name__}, State: Accessing {model_filename}, start")
        with open(model_filename, 'wb') as file:
            pickle.dump(self.classifier, file)
        self.logger.debug(f"Object: {TipQCDetector.__name__}, method: {TipQCDetector.Train.__name__}, State: Accessing {model_filename}, end")
        
        imgSegmented = future.predict_segmenter(first_img_features, self.classifier)
        self.visionCommon.SaveImage(imgSegmented, 'bin-roi-trainSegmented', segmentation=True)
        self.logger.debug(f"Object: {TipQCDetector.__name__}, method: {TipQCDetector.Train.__name__}, end")
    
    
    def ExecuteTipQCClassification(self, roiImage):
        self.logger.debug(f"Object: {TipQCDetector.__name__}, method: {TipQCDetector.ExecuteTipQCClassification.__name__}, start")
        
        features = self.features_func(roiImage)
        imgSegmented = future.predict_segmenter(features, self.classifier)
        self.visionCommon.SaveImage(imgSegmented, 'bin_clean_roi_segmented', segmentation=True)
        
        imgBoundary = self.boundaryProcessor.Execute(imgSegmented)
        self.visionCommon.SaveImage(imgBoundary, 'bin_clean_roi_segmented_boundary', boundary=True)
        
        # Inner circle analysis
        innerCircleRegion = imgSegmented == 3
        scoreInnerCircle = self.circleChecker.Analyze(innerCircleRegion)
        self.visionCommon.SaveImage(innerCircleRegion, f'bin_clean_roi_segmented_inner-circle_{scoreInnerCircle:.4f}', circle=True)
        
        # Outer circle analysis 
        outerCircleRegion = imgSegmented == 2
        scoreOuterCircle = self.circleChecker.Analyze(outerCircleRegion)
        # self.visionCommon.SaveImage(outerCircleRegion, f'bin_clean_roi_segmented_outer-circle_{scoreOuterCircle:.4f}', circle=True)       
        
        label = self.FinalClassifier(scoreInnerCircle, scoreOuterCircle)
        
        self.logger.debug(f"Object: {TipQCDetector.__name__}, method: {TipQCDetector.ExecuteTipQCClassification.__name__}, end")
        return label
    
    
    def FinalClassifier(self, scoreInnerCircle, scoreOuterCircle):
        if scoreInnerCircle < 0.4:
            self.logger.debug(f"Object: {TipQCDetector.__name__}, method: {TipQCDetector.FinalClassifier.__name__}, Label: {Label.NG.name},  end")
            return Label.NG
        elif scoreInnerCircle > 0.8:
            return Label.AG
        return Label.Undefined