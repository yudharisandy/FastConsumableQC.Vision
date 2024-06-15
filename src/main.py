from VisionWrapper import VisionWrapper
from Common.Logger import Logger
import logging
import os

if __name__ == "__main__":
    
    Logger.setup_logging()
    
    logger = logging.getLogger(__name__)
    
    logger.debug('Main is starting')

    visionWrapper = VisionWrapper()
    
    # Execute by using a camera stream
    # result = visionWrapper.ExecuteTipQCClassification()
    
    # Execute a single image
    # folderPath = 'dataset'
    # imageName = '965.png'
    # imagePath = os.path.join(folderPath, imageName)
    # result = visionWrapper.ExecuteTipQCClassification(imagePath)
    
    # Execute many images in a folder
    folderPath = 'dataset'
    result = visionWrapper.ExecuteTipQClassificationOnFolder(folderPath)
    
    logger.debug("Main end.")