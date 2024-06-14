import cv2
from skimage import io
import os
import logging

class FrameGrabber:
    def __init__(self, camera_index=0):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(f"Object: {FrameGrabber.__name__} was created")
        
        self.cap = cv2.VideoCapture(camera_index)
        if not self.cap.isOpened():
            raise Exception("Could not open video device")
        
        # Modify these variables to run whether on an image or using camera stream
        self.imageFileName = '6812.png'
        self.imagePath = os.path.join('dataset', self.imageFileName) # Set self.imagePath to None for using camera stream
        # self.imagePath = None 

    def GrabFrame(self):
        self.logger.debug(f"Object: {FrameGrabber.__name__}, method: {FrameGrabber.GrabFrame.__name__}, start")
        
        if self.imagePath is None:
            self.ret, self.frame = self.cap.read()
            if not self.ret:
                raise Exception("Could not read frame")
            return self.frame
        
        image = io.imread(self.imagePath)
        
        self.logger.debug(f"Object: {FrameGrabber.__name__}, method: {FrameGrabber.GrabFrame.__name__}, end")
        return image
    
    
    def GrabFrameFolder(self, folder):
        self.logger.debug(f"Object: {FrameGrabber.__name__}, method: {FrameGrabber.GrabFrameFolder.__name__}, start")
        
        imagePaths = [f for f in os.listdir(folder) if f.endswith(('.png', '.jpg', '.jpeg'))]
        images = []
        
        for imagePath in imagePaths:
            images.append(io.imread(os.path.join(folder, imagePath)))
        
        self.logger.debug(f"Object: {FrameGrabber.__name__}, method: {FrameGrabber.GrabFrameFolder.__name__}, end")
        return images
            

    def GrabFrameToTrain(self, imageToTrainFileName):
        self.logger.debug(f"Object: {FrameGrabber.__name__}, method: {FrameGrabber.GrabFrameToTrain.__name__}, start")
        
        imageToTrain = io.imread(imageToTrainFileName)
        
        self.logger.debug(f"Object: {FrameGrabber.__name__}, method: {FrameGrabber.GrabFrameToTrain.__name__}, end")
        return imageToTrain
    
        
    def __del__(self):
        if self.cap.isOpened():
            self.cap.release()
    
    
    def ShowFrame(self):
        self.logger.debug(f"Object: {FrameGrabber.__name__}, method: {FrameGrabber.ShowFrame.__name__}, start")
        
        cv2.imshow("FAST QC Consumable", self.frame)
        
        self.logger.debug(f"Object: {FrameGrabber.__name__}, method: {FrameGrabber.ShowFrame.__name__}, end")