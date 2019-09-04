from abc import abstractmethod

from search_ai.ga.replace_duplicates.replace_duplicates import ReplaceDuplicates


class ReplaceDuplicatesWithFitness(ReplaceDuplicates):

    def __init__(self, fitness):
        super(ReplaceDuplicatesWithFitness, self).__init__()
        self._fitness = fitness

    @property
    def fitness(self):
        return self._fitness

    @fitness.setter
    def fitness(self, fitness):
        self._fitness = fitness
    