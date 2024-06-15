import logging
import numpy as np
from skimage import morphology

class SmallObjectRemover:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(f"Object: {SmallObjectRemover.__name__} was created")
    
    
    def Execute(self, binaryImage):
        self.logger.debug(f"Object: {SmallObjectRemover.__name__}, method: {SmallObjectRemover.Execute.__name__}, start")
        
        binaryImageClean = morphology.remove_small_objects(binaryImage, min_size=500)
        binaryImageClean = (binaryImageClean * 255).astype(np.uint8)
        
        self.logger.debug(f"Object: {SmallObjectRemover.__name__}, method: {SmallObjectRemover.Execute.__name__}, end")
        return binaryImageClean