import os
import cv2
from datetime import datetime
import logging

class VisionCommon:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(f"Object: {VisionCommon.__name__} was created")
    
    def SaveImage(self, image, processingType, segmentation=False):
        self.logger.debug(f"Object: {VisionCommon.__name__}, method: {VisionCommon.SaveImage.__name__}, start")
        
        folder_path = 'image_dump'
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S%f')[:-2]
        file_name = f'{current_time}_{processingType}.png'
        file_path = os.path.join(folder_path, file_name)
        
        if not segmentation:    
            cv2.imwrite(file_path, image)
        else:
            scaled_image = image * 85
            cv2.imwrite(file_path, scaled_image)
        self.logger.debug(f"Object: {VisionCommon.__name__}, method: {VisionCommon.SaveImage.__name__}, State: Image saved as {file_path}")
        
        self.logger.debug(f"Object: {VisionCommon.__name__}, method: {VisionCommon.SaveImage.__name__}, end")