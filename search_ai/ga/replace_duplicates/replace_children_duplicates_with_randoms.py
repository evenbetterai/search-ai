import random as rd

from search_ai.ga.replace_duplicates.replace_duplicates import ReplaceDuplicates


class ReplaceChildrenDuplicatesWithRandoms(ReplaceDuplicates):

    def __init__(self, fitness):
        super(ReplaceChildrenDuplicatesWithRandoms, self).__init__(fitness)

    # Population not used
    def replace_child(self, population, children, child_index):
        new_child = self._fitness.new_random_individual()
        self._fitness.run(new_child)
        children[child_index] = new_child
