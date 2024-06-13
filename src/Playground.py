import os
import pickle
from basic_image_processor.roi_processor import ROIProcessor
from tip_qc_detection.tip_qc_detection import TipQCDetector
from sklearn.ensemble import RandomForestClassifier

class Playground:
  def __init__(self, dataset, isFolder=False, isTrain=False):
    print(f"Object: {Playground.__name__} was created, isFolder: {isFolder}")
    
    self.dataset = dataset
    self.isTrain = isTrain
    self.isFolder = isFolder
    
    self.roiProcessor = ROIProcessor(isFolder)
    self.tipQCDetector = TipQCDetector(isTrain, isFolder)
    
    if(isFolder):  
      self.image_files = [f for f in os.listdir(dataset) if f.endswith(('.png', '.jpg', '.jpeg'))]
    else:
      self.image_files = [dataset]
    print(f"Image files: {self.image_files}")
    
  
  def ExecuteClassification(self):
    roi_images = self.roiProcessor.Execute(self.image_files, self.dataset)
    
    if(self.isTrain):
      self.tipQCDetector.Train(roi_images['965.png'], '965.png')
    
    self.tipQCDetector.ExecuteClassification(roi_images)
    