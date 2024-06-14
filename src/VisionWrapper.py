from Playground import Playground
from Utils.FrameGrabber import FrameGrabber
import logging
import os
from Common.Label import Label

class VisionWrapper:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(f"Object: {VisionWrapper.__name__} was created")
        
        self.isTrainTipQC = False
        self.playground = Playground(self.isTrainTipQC)
        self.frameGrabber = FrameGrabber()
    
    
    def ExecuteTipQCClassification(self, imagePath=None):
        self.logger.debug(f"Object: {VisionWrapper.__name__}, method: {VisionWrapper.ExecuteTipQCClassification.__name__}, start")
    
        rawImage = self.frameGrabber.GrabFrame(imagePath)
        # self.frameGrabber.ShowFrame()
        
        if(self.isTrainTipQC):
            label = self.playground.TrainTipQCClassification('dataset\\965.png')
        else:
            label = self.playground.ExecuteTipQCClassification(rawImage)
        
        self.ShowResult(label, imagePath) # Temporary

        self.logger.debug(f"Object: {VisionWrapper.__name__}, method: {VisionWrapper.ExecuteTipQCClassification.__name__}, end")
        
        return label
    
    
    def ExecuteTipQClassificationOnFolder(self, folder):
        self.logger.debug(f"Object: {VisionWrapper.__name__}, method: {VisionWrapper.ExecuteTipQCClassification.__name__}, start")

        imagePaths = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith(('.png', '.jpg', '.jpeg'))]

        for imagePath in imagePaths:
            rawImage = self.frameGrabber.GrabFrame(imagePath)
            label = self.playground.ExecuteTipQCClassification(rawImage)
            self.ShowResult(label, imagePath) # Temporary
            
        self.logger.debug(f"Object: {VisionWrapper.__name__}, method: {VisionWrapper.ExecuteTipQCClassification.__name__}, end")
    
    
    def ShowResult(self, label, imagePath=None):
        labelImage = ''
        
        if label == Label.G:
            labelImage = Label.G.name
        elif label == Label.AG:
            labelImage = Label.AG.name
        elif label == Label.NG:
            labelImage = Label.NG.name
        else:
            labelImage = Label.Undefined.name

        self.PrintResult(labelImage, imagePath)
    
    def PrintResult(self, label , imagePath=None):
        if imagePath is not None:
            print(f"Image: {imagePath} | Label: {label}")
            self.logger.info(f"Object: {VisionWrapper.__name__}, method: {VisionWrapper.PrintResult.__name__}, Result, Image: {imagePath}, Label: {label}")
        else:
            print(f"Label: {label}")
            self.logger.info(f"Object: {VisionWrapper.__name__}, method: {VisionWrapper.PrintResult.__name__}, Result, Label: {label}")