from abc import abstractmethod

from search_ai.ga.replace_duplicates.replace_duplicates import ReplaceDuplicates
from search_ai.utils.search import Search

class ReplaceChildrenDuplicates(ReplaceDuplicates):

    def __init__(self, fitness):
        super(ReplaceChildrenDuplicates, self).__init__(fitness)

    @abstractmethod
    def replace_child(self, population, children, child_index):
        pass

    def run(self, population, children):
        for i in range(len(children)):
            if Search.sequencial_search(population, children[i], lambda ind: ind.features) > -1:
                self.replace_child(population, children, i)
