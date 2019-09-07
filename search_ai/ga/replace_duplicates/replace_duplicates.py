from abc import ABC, abstractmethod

from search_ai.utils.search import Search


class ReplaceDuplicates(ABC):

    def __init__(self, fitness):
        self._fitness = fitness

    @property
    def fitness(self):
        return self._fitness

    @fitness.setter
    def fitness(self, fitness):
        self._fitness = fitness

    @abstractmethod
    def run(self, population, children):
        pass
