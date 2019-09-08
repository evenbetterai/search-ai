from abc import abstractmethod

from search_ai.ga.replace_duplicates.replace_duplicates import ReplaceDuplicates
from search_ai.utils.search import Search

class ReplacePopulationDuplicates(ReplaceDuplicates):

    def __init__(self, replacer):
        super(ReplacePopulationDuplicates, self).__init__(replacer)

    def run(self, **kwargs):
        self._population = kwargs['population']

        for i in range(len(self._population)):
            others = list(self._population)
            others.pop(i)

            if Search.sequencial_search(others, self._population[i], ReplaceDuplicates.cmp_by_features) > -1:
                self._replacer.replace_in_population(self, i)   

    