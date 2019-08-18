import random as rd

from search_ai.ga.replace_duplicates.replace_duplicates import ReplaceDuplicates


class ReplaceDuplicatesWithRandoms(ReplaceDuplicates):

    def __init__(self, fitness):
        super(ReplaceDuplicatesWithRandoms, self).__init__()
        self._fitness = fitness

    def replace_child(self, population, index):
        population[index] = self._fitness.new_random_individual()
