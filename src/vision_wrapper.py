from playground import Playground

class VisionWrapper:
  def __init__(self, dataset, isFolder=False, isTrain=False):
    print(f"Object: {VisionWrapper.__name__} was created, isFolder: {isFolder}")
    self.playground = Playground(dataset, isFolder, isTrain)
  
  def ExecuteTipQCClassification(self):
    print(f"Object: {VisionWrapper.__name__}, method: {VisionWrapper.ExecuteTipQCClassification.__name__}, start")
    self.playground.ExecuteTipQCClassification()
    print(f"Object: {VisionWrapper.__name__}, method: {VisionWrapper.ExecuteTipQCClassification.__name__}, end")