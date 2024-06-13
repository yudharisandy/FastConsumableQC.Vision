from playground import Playground

class VisionWrapper:
  def __init__(self, dataset_folder):
    self.playground = Playground(dataset_folder)
  
  def ExecuteClassification(self):
    self.playground.ExecuteClassification()