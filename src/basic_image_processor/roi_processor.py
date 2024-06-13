import os
import numpy as np
import matplotlib.pyplot as plt
from skimage import io, segmentation, feature, future, color, filters, morphology
from sklearn.ensemble import RandomForestClassifier
from functools import partial
import cv2

from basic_image_processor.vision_common import VisionCommon

class ROIProcessor:
  def __init__(self, isFolder=False):
    print(f"Object: {ROIProcessor.__name__} was created")
    self.isFolder = isFolder
    self.roi_images = {}
    self.visionCommon = VisionCommon()
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
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        return largest_contour
    else:
        return None

  def get_bounding_box(self, contour):
    x, y, w, h = cv2.boundingRect(contour)
    return x, y, w, h
  
  def Execute(self, image_files, dataset_folder):
    print(f"Object: {ROIProcessor.__name__}, method: {ROIProcessor.Execute.__name__}, start")
    
    for image_filename in image_files:
        if(self.isFolder):
          image_path = os.path.join(dataset_folder, image_filename)
        else:
          image_path = image_files[0]
          
        img = io.imread(image_path)

        gray_img = color.rgb2gray(img)

        thresh = filters.threshold_otsu(gray_img)
        binary_img = gray_img > thresh

        binary_img_uint8 = (binary_img * 255).astype(np.uint8)

        binary_img_clean = morphology.remove_small_objects(binary_img, min_size=500)
        binary_img_clean = (binary_img_clean * 255).astype(np.uint8)
        
        if(self.isFolder):
          self.visionCommon.save_image(binary_img_clean, image_filename, 'bin', isFolder=self.isFolder)
        else:
          self.visionCommon.save_image(binary_img_clean, image_files[0], 'bin')

        # Get the largest contour
        largest_contour = self.get_largest_contour(binary_img_clean)

        if largest_contour is not None:
            x, y, w, h = self.get_bounding_box(largest_contour)
            roi_img = img[y:y+h, x:x+w]
            
            self.visionCommon.save_image(roi_img, image_filename, 'bin_ROI', isFolder = self.isFolder)
            
            self.roi_images[image_filename] = roi_img
        else:
            print(f"No valid ROI found for {image_filename}")
                
    print(f"Object: {ROIProcessor.__name__}, method: {ROIProcessor.Execute.__name__}, end")
    return self.roi_images
  