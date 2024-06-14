from BasicImageProcessor.RoiProcessor import ROIProcessor
from TipQCDetection.TipQCDetection import TipQCDetector
from FrameGrabber import FrameGrabber
import logging

class Playground:
    def __init__(self, isTrainTipQC):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(f"Object: {Playground.__name__} was created")
        
        self.roiProcessor = ROIProcessor()
        self.tipQCDetector = TipQCDetector(isTrainTipQC)
    
    def ExecuteTipQCClassification(self, rawImage):
        self.logger.debug(f"Object: {Playground.__name__}, method: {Playground.ExecuteTipQCClassification.__name__}, start")
        
        roiImage = self.roiProcessor.Execute(rawImage)
        if(roiImage is not None): 
            self.tipQCDetector.ExecuteTipQCClassification(roiImage)
        
        self.logger.debug(f"Object: {Playground.__name__}, method: {Playground.ExecuteTipQCClassification.__name__}, end")
    
    def TrainTipQCClassification(self, imagePathToTrain):
        self.logger.debug(f"Object: {Playground.__name__}, method: {Playground.TrainTipQCClassification.__name__}, start")
        
        frameGrabberToTrain = FrameGrabber()
        rawImageToTrain = frameGrabberToTrain.GrabFrameToTrain(imagePathToTrain)
        roiImageToTrain = self.roiProcessor.Execute(rawImageToTrain)
        self.tipQCDetector.Train(roiImageToTrain)
        del frameGrabberToTrain
        
        self.logger.debug(f"Object: {Playground.__name__}, method: {Playground.TrainTipQCClassification.__name__}, end")