import os
import cv2

class VisionCommon:
  def save_image(self, image, image_name, step_type):
    folder_path = 'ImageDump'
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    if image_name.endswith('.png'):
        image_name = image_name[:-4]

    file_path = os.path.join(folder_path, f'{image_name}_{step_type}.png')
    cv2.imwrite(file_path, image)