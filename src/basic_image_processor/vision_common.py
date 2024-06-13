import os
import cv2
import matplotlib.pyplot as plt

class VisionCommon:
  def __init__(self):
    print(f"Object: {VisionCommon.__name__} was created")
  
  def save_image(self, image, image_name, step_type, segmentation=False, isFolder=False):
    folder_path = 'image_dump'
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    if image_name.endswith('.png'):
        image_name = image_name[:-4]

    if(isFolder is not True):
      image_name = image_name[12:]

    file_path = os.path.join(folder_path, f'{image_name}_{step_type}.png')
    
    if segmentation == False:    
      cv2.imwrite(file_path, image)
    else:
      scaled_image = image * 85
      cv2.imwrite(file_path, scaled_image)