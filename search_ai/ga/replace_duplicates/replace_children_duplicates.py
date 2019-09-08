from abc import abstractmethod

from search_ai.ga.replace_duplicates.replace_duplicates import ReplaceDuplicates
from search_ai.utils.search import Search

class ReplaceChildrenDuplicates(ReplaceDuplicates):

    def __init__(self, fitness):
        super(ReplaceChildrenDuplicates, self).__init__(fitness)
        self._population = None
        self._children = None

    @abstractmethod
    def replace_child(self, index):
        pass

    def run(self, **kwargs):
        self._population = kwargs['population']
        self._children = kwargs['children']

        for i in range(len(self._children)):
            if Search.sequencial_search(self._population, self._children[i], lambda ind: ind.features) > -1:
                self.replace_child(i)
