from skimage import draw
import logging

class BoundingBoxDrawer:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.debug(f"Object: {BoundingBoxDrawer.__name__} was created")
        
    def Execute(self, image, x, y, w, h):
        
        rr, cc = draw.rectangle_perimeter(start=(y, x), extent=(h, w), shape=image.shape)
        image[rr, cc] = (0, 255, 0)
        
        return image