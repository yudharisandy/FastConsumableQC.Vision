import os
from basic_image_processor.roi_processor import ROIProcessor

class Playground:
  def __init__(self, dataset_folder):
    self.dataset_folder = dataset_folder
    self.image_files = [f for f in os.listdir(dataset_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]
    print(f"Image files: {self.image_files}")
    self.roiProcessor = ROIProcessor()
  
  def ExecuteClassification(self):
    self.roiProcessor.Execute(self.image_files, self.dataset_folder)