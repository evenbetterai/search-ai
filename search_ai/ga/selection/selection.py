from abc import ABC, abstractmethod


class Selection(ABC):

    def __init__(self, num_of_parents):
        self._number_of_parents = num_of_parents

    @abstractmethod
    def run(self, population):
        pass
