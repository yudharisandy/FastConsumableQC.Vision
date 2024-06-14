from Playground import Playground
from Utils.FrameGrabber import FrameGrabber
import logging

class VisionWrapper:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(f"Object: {VisionWrapper.__name__} was created")
        
        self.isTrainTipQC = False
        self.playground = Playground(self.isTrainTipQC)
        self.frameGrabber = FrameGrabber()
    
    
    def ExecuteTipQCClassification(self):
        self.logger.debug(f"Object: {VisionWrapper.__name__}, method: {VisionWrapper.ExecuteTipQCClassification.__name__}, start")
    
        rawImage = self.frameGrabber.GrabFrame()
        # self.frameGrabber.ShowFrame()
        
        if(self.isTrainTipQC):
            self.playground.TrainTipQCClassification('dataset\\965.png')
        else:
            self.playground.ExecuteTipQCClassification(rawImage)
        
        self.logger.debug(f"Object: {VisionWrapper.__name__}, method: {VisionWrapper.ExecuteTipQCClassification.__name__}, end")
    
    
    def ExecuteTipQClassificationOnFolder(self, folder):
        self.logger.debug(f"Object: {VisionWrapper.__name__}, method: {VisionWrapper.ExecuteTipQCClassification.__name__}, start")
    
        rawImages = self.frameGrabber.GrabFrameFolder(folder)

        for rawImage in rawImages:
            self.playground.ExecuteTipQCClassification(rawImage)
        
        self.logger.debug(f"Object: {VisionWrapper.__name__}, method: {VisionWrapper.ExecuteTipQCClassification.__name__}, end")