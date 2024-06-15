import os
import cv2
from datetime import datetime
import logging

class VisionCommon:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(f"Object: {VisionCommon.__name__} was created")
    
    def SaveImage(self, image, processingType, segmentation=False, circle=False, boundary=False):
        self.logger.debug(f"Object: {VisionCommon.__name__}, method: {VisionCommon.SaveImage.__name__}, start")
        
        folder_path = 'log'
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S%f')[:-2]
        file_name = f'{current_time}_{processingType}.png'
        file_path = os.path.join(folder_path, file_name)
        
        if segmentation:
            scaled_image = image * 85
            cv2.imwrite(file_path, scaled_image)    
        elif circle:
            scaled_image = image * 255
            cv2.imwrite(file_path, scaled_image)   
        elif boundary:
            scaled_image = image * 255
            cv2.imwrite(file_path, scaled_image)   
        else:
            cv2.imwrite(file_path, image)
        
        
        self.logger.debug(f"Object: {VisionCommon.__name__}, method: {VisionCommon.SaveImage.__name__}, State: Image saved as {file_path}")
        
        self.logger.debug(f"Object: {VisionCommon.__name__}, method: {VisionCommon.SaveImage.__name__}, end")