from abc import ABC, abstractmethod

class Recombination(ABC):
  def __init__(self, fitness, num_of_children):
    self._fitness = fitness
    self._number_of_children = num_of_children

  @property
  def fitness(self):
    return self._fitness

  @fitness.setter
  def fitness(self, new_fitness):
    self._fitness = new_fitness

  @property
  def number_of_children(self):
    return self._number_of_children

  @number_of_children.setter
  def num_of_children(self, new_value):
    if new_value <= 1:
      raise ValueError('\'num_of_children\' attribute has to hold' + \
                       'a number greater or equal to \'1\'')

    self._number_of_children = new_value

  @abstractmethod
  def run(self, parents):
    pass
