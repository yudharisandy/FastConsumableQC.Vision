from LowLevelProcessor.RoiProcessor import ROIProcessor
from HighLevelProcessor.TipQCDetector import TipQCDetector
from Utils.FrameGrabber import FrameGrabber
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
        label = None
        if(roiImage is not None): 
            label = self.tipQCDetector.ExecuteTipQCClassification(roiImage)
        
        self.logger.debug(f"Object: {Playground.__name__}, method: {Playground.ExecuteTipQCClassification.__name__}, end")
        
        return label
    
    def TrainTipQCClassification(self, imagePathToTrain):
        self.logger.debug(f"Object: {Playground.__name__}, method: {Playground.TrainTipQCClassification.__name__}, start")
        
        frameGrabberToTrain = FrameGrabber()
        rawImageToTrain = frameGrabberToTrain.GrabFrameToTrain(imagePathToTrain)
        roiImageToTrain = self.roiProcessor.Execute(rawImageToTrain)
        self.tipQCDetector.Train(roiImageToTrain)
        del frameGrabberToTrain
        
        self.logger.debug(f"Object: {Playground.__name__}, method: {Playground.TrainTipQCClassification.__name__}, end")