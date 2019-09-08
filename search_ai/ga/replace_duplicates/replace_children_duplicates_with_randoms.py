import random as rd

from search_ai.ga.replace_duplicates.replace_children_duplicates import ReplaceChildrenDuplicates


class ReplaceChildrenDuplicatesWithRandoms(ReplaceChildrenDuplicates):

    def __init__(self, fitness):
        super(ReplaceChildrenDuplicatesWithRandoms, self).__init__(fitness)

    def replace_child(self, index):
        new_child = self._fitness.new_random_individual()
        self._fitness.run(new_child)
        self._children[index] = new_child
