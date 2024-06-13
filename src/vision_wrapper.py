from playground import Playground

class VisionWrapper:
  def __init__(self, dataset, isFolder=False, isTrain=False):
    print(f"Object: {VisionWrapper.__name__} was created, isFolder: {isFolder}")
    self.playground = Playground(dataset, isFolder, isTrain)
  
  def ExecuteClassification(self):
    print(f"Object: {VisionWrapper.__name__}, method: {VisionWrapper.ExecuteClassification.__name__}, start")
    self.playground.ExecuteClassification()
    print(f"Object: {VisionWrapper.__name__}, method: {VisionWrapper.ExecuteClassification.__name__}, end")