import logging
from skimage import segmentation
import numpy as np

class BoundaryProcessor:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(f"Object: {BoundaryProcessor.__name__} was created")
    
    
    def Execute(self, imgSegmented):
        self.logger.debug(f"Object: {BoundaryProcessor.__name__}, method: {BoundaryProcessor.Execute.__name__}, start")
        
        imgBoundary = segmentation.mark_boundaries(np.zeros((imgSegmented.shape[0], imgSegmented.shape[1]), dtype=np.uint8), imgSegmented, mode='inner')
        
        self.logger.debug(f"Object: {BoundaryProcessor.__name__}, method: {BoundaryProcessor.Execute.__name__}, end")
        return imgBoundary