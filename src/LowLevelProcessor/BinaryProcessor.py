import logging
import numpy as np
from skimage import morphology, filters

class BinaryProcessor:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(f"Object: {BinaryProcessor.__name__} was created")
    
    
    def Execute(self, greyImage):
        self.logger.debug(f"Object: {BinaryProcessor.__name__}, method: {BinaryProcessor.Execute.__name__}, start")
        
        thresh = filters.threshold_otsu(greyImage)
        binaryImage = greyImage > thresh
        
        self.logger.debug(f"Object: {BinaryProcessor.__name__}, method: {BinaryProcessor.Execute.__name__}, start")
        return binaryImage