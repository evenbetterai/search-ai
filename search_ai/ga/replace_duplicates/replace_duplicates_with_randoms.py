import random as rd

from search_ai.ga.replace_duplicates.replace_duplicates import ReplaceDuplicates


class ReplaceDuplicatesWithRandoms(ReplaceDuplicates):

    def __init__(self, fitness):
        super(ReplaceDuplicatesForRandoms, self).__init__()
        self._fitness = fitness

    def replace_child(self, children, index):
        children[index] = self._fitness.new_random_individual()
