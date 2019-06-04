from abc import ABC, abstractmethod

class InitializationComponent(ABC):
  def __init__(self):
    pass

  @abstractmethod
  def run(self):
    pass
