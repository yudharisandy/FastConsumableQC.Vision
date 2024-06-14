from VisionWrapper import VisionWrapper
from Common.Logger import Logger
import logging

if __name__ == "__main__":
    
    Logger.setup_logging()
    
    logger = logging.getLogger(__name__)
    
    logger.debug('Main is starting')

    visionWrapper = VisionWrapper()
    
    # Execute one frame whether from a file or a camera stream
    # For executing using camera stream, look at the constructor of FrameGrabber object
    # tipQCClassificationResult = visionWrapper.ExecuteTipQCClassification()

    # Execute one folder
    dataset_folder = 'dataset'
    tipQCClassificationFolderResult = visionWrapper.ExecuteTipQClassificationOnFolder(dataset_folder)
    
    logger.debug("Main end.")