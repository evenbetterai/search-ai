from abc import abstractmethod

from search_ai.ga.replace_duplicates.replace_duplicates import ReplaceDuplicates
from search_ai.utils.search import Search


class ReplaceChildrenDuplicates(ReplaceDuplicates):
    
    def __init__(self, replacer):
        super(ReplaceChildrenDuplicates, self).__init__(replacer)
        self._children = None
    
    def run(self, **kwargs):
        self._population = kwargs['population']
        self._children = kwargs['children']
        
        for i in range(len(self._children)):
            if Search.sequencial_search(
                    self._population,
                    self._children[i],
                    ReplaceDuplicates.cmp_by_features) > -1:
                self._replacer.replace_in_children(self, i)
