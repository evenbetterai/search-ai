from abc import ABC, abstractmethod


class Replacer(ABC):

    def __init__(self, fitness):
        self._fitness = fitness

    @property
    def fitness(self):
        return self._fitness

    @fitness.setter
    def fitness(self, fitness):
        self._fitness = fitness

    @abstractmethod
    def get_new_individual(self):
        pass

    @abstractmethod
    def replace_in_population(self, replace_duplicates):
        pass

    @abstractmethod
    def replace_in_children(self, replace_duplicates):
        pass

