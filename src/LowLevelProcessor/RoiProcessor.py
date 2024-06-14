import numpy as np
from skimage import feature, filters, morphology
from functools import partial
import cv2
import logging
from Common.VisionCommon import VisionCommon
from LowLevelProcessor.GreyProcessor import GreyProcessor

class ROIProcessor:
  def __init__(self):
    self.logger = logging.getLogger(__name__)
    self.logger.debug(f"Object: {ROIProcessor.__name__} was created")

    self.roiImage = None
    self.visionCommon = VisionCommon()
    self.greyProcessor = GreyProcessor()
    
    sigma_min = 1
    sigma_max = 16
    self.features_func = partial(
        feature.multiscale_basic_features,
        intensity=True,
        edges=True,
        texture=True,
        sigma_min=sigma_min,
        sigma_max=sigma_max,
        channel_axis=-1,
    )

  def get_largest_contour(self, binary_image):
    self.logger.debug(f"Object: {ROIProcessor.__name__}, method: {ROIProcessor.get_largest_contour.__name__}, start")
    
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        self.logger.debug(f"Object: {ROIProcessor.__name__}, method: {ROIProcessor.get_largest_contour.__name__}, contours exist, end")
        return largest_contour
    else:
        self.logger.debug(f"Object: {ROIProcessor.__name__}, method: {ROIProcessor.get_largest_contour.__name__}, contours none, end")
        return None

  def get_bounding_box(self, contour):
    self.logger.debug(f"Object: {ROIProcessor.__name__}, method: {ROIProcessor.get_bounding_box.__name__}, start")
    
    x, y, w, h = cv2.boundingRect(contour)
    self.logger.debug(f"Object: {ROIProcessor.__name__}, method: {ROIProcessor.get_bounding_box.__name__}, Result x: {x}, y: {y}, w: {w}, h: {h}")
    
    self.logger.debug(f"Object: {ROIProcessor.__name__}, method: {ROIProcessor.get_bounding_box.__name__}, end")
    return x, y, w, h
  
  def Execute(self, rawImage):
    self.logger.debug(f"Object: {ROIProcessor.__name__}, method: {ROIProcessor.Execute.__name__}, start")

    gray_img = self.greyProcessor.Execute(rawImage)

    thresh = filters.threshold_otsu(gray_img)
    binary_img = gray_img > thresh

    binary_img_uint8 = (binary_img * 255).astype(np.uint8)

    binary_img_clean = morphology.remove_small_objects(binary_img, min_size=500)
    binary_img_clean = (binary_img_clean * 255).astype(np.uint8)
    
    self.visionCommon.SaveImage(binary_img_clean, 'bin')

    largest_contour = self.get_largest_contour(binary_img_clean)

    if largest_contour is not None:
        x, y, w, h = self.get_bounding_box(largest_contour)
        self.roiImage = rawImage[y:y+h, x:x+w]
        self.visionCommon.SaveImage(self.roiImage, 'bin-roi')
    else:
        self.logger.debug(f"Object: {ROIProcessor.__name__}, method: {ROIProcessor.Execute.__name__}, Result: No valid ROI found for this frame")
                
    self.logger.debug(f"Object: {ROIProcessor.__name__}, method: {ROIProcessor.Execute.__name__}, end")
    
    return self.roiImage
  