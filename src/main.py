from VisionWrapper import VisionWrapper
from Common.Logger import Logger
from Common.JsonLoader import JsonLoader
from Common.RunningMode import RunningMode
import logging
import os

if __name__ == "__main__":
    Logger.setup_logging()
    logger = logging.getLogger(__name__)
    logger.debug('Main is starting')

    jsonLoader = JsonLoader()
    config = jsonLoader.LoadConfig('config/config.json')

    visionWrapper = VisionWrapper(config)
    
    mode = config.get("runningMode")

    if mode == RunningMode.Camera.name:
        result = visionWrapper.ExecuteTipQCClassification()
    elif mode == RunningMode.File.name:
        folderPath = config.get("folderPath")
        imageName = config.get("imagePath")
        imagePath = os.path.join(folderPath, imageName)
        result = visionWrapper.ExecuteTipQCClassification(imagePath)
    elif mode == RunningMode.Folder.name:
        folderPath = config.get("folderPath")
        result = visionWrapper.ExecuteTipQClassificationOnFolder(folderPath)
    else:
        logger.debug('Undefined mode!')
    
    logger.debug("Main end.")