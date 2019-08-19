from abc import ABC, abstractmethod


class Elitism(ABC):

    def __init__(self, k):
        self.k = k

    @property
    def k(self):
        return self._k

    @k.setter
    def k(self, k):
        if (k < 1):
            raise ValueError('\'k\' has to be a value greater than 0')

        self._k = k

    @abstractmethod
    def run(self, population, children):
        pass
