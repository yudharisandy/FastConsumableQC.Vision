import numpy as np
import pickle
from functools import partial
from skimage import io, segmentation, feature, future, color, filters, morphology
from sklearn.ensemble import RandomForestClassifier
from basic_image_processor.vision_common import VisionCommon

class TipQCDetector:
    def __init__(self, isTrain=False, isFolder=False):
        print(f"Object: {TipQCDetector.__name__} was created")
        
        self.isTrain = isTrain
        self.isFolder = isFolder
        self.visionCommon = VisionCommon()
        
        if(self.isTrain):
            self.classifier = RandomForestClassifier()
        else:
            with open('models/model.pkl', 'rb') as file:
                self.classifier = pickle.load(file)

        self.segmentation_images = {}
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

    def Train(self, imgToTrain, image_name):
        print(f"Object: {TipQCDetector.__name__}, method: {TipQCDetector.Train.__name__}, start")
        height, width = imgToTrain.shape[:2]

        training_labels = np.zeros((height, width), dtype=np.uint8)
        training_labels[150:220, 140:210] = 1 # black background
        training_labels[20:90, 120:220] = 2 # tip body
        training_labels[270:340, 125:220] = 2 # tip body
        training_labels[130:230, 270:330] = 2 # tip body
        training_labels[130:250, 30:90] = 2 # tip body
        training_labels[155:215, 238:255] = 3 # plunger (white section)
        training_labels[120:140, 210:230] = 3 # plunger (white section)
        
        first_img_features = self.features_func(imgToTrain)
        self.classifier = future.fit_segmenter(training_labels, first_img_features, self.classifier)
        
        model_filename = 'models/model.pkl'
        with open(model_filename, 'wb') as file:
            pickle.dump(self.classifier, file)
        
        imgSegmented = future.predict_segmenter(first_img_features, self.classifier)
        self.visionCommon.save_image(imgSegmented, image_name, 'bin_ROI_trainSegmented', segmentation=True, isFolder=self.isFolder)
        
        print(f"Object: {TipQCDetector.__name__}, method: {TipQCDetector.Train.__name__}, end")
    
    
    def ExecuteClassification(self, roi_images):
        print(f"Object: {TipQCDetector.__name__}, method: {TipQCDetector.ExecuteClassification.__name__}, start")
        
        for roi_image_name in roi_images.keys():
            img = roi_images[roi_image_name]
            features = self.features_func(img)
            imgSegmented = future.predict_segmenter(features, self.classifier)

            self.segmentation_images[roi_image_name] = imgSegmented
            
            self.visionCommon.save_image(imgSegmented, roi_image_name, 'bin_ROI_segmented', segmentation=True, isFolder=self.isFolder)
        
        print(f"Object: {TipQCDetector.__name__}, method: {TipQCDetector.ExecuteClassification.__name__}, end")