from abc import ABC, abstractmethod

class ReplaceDuplicates(ABC):
  def __init__(self):
    pass

  @abstractmethod
  def replace_child(self, children, index):
    pass

  def run(self, population, children):
    for index in range(len(children)):
      while children[index] in population:
        self.replace_child(children, index)
