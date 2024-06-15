from skimage import color
import logging

class GreyProcessor:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(f"Object: {GreyProcessor.__name__} was created")
        
        
    def Execute(self, image3D):
        greyImage = color.rgb2gray(image3D)
        return greyImage