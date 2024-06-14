import numpy as np
import logging
from Common.VisionCommon import VisionCommon

class CircleChecker:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(f"Object: {CircleChecker.__name__} was created")
        
        self.visionCommon = VisionCommon()
    
    
    def Analyze(self, circleRegion):
        self.logger.debug(f"Object: {CircleChecker.__name__}, method: {CircleChecker.Analyze.__name__}, start")
        
        circularity = (4 * np.pi * circleRegion.sum()) / (circleRegion.shape[0] * circleRegion.shape[1])
        score = 1 - abs(circularity - 1)
        
        self.logger.debug(f"Object: {CircleChecker.__name__}, method: {CircleChecker.Analyze.__name__}, circularity: {circularity}, score: {score}, end")
        return score