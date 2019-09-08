from abc import abstractmethod

from search_ai.ga.replace_duplicates.replace_duplicates import ReplaceDuplicates

class ReplacePopulationDuplicates(ReplaceDuplicates):

    def __init__(self, fitness):
        super(ReplacePopulationDuplicates, self).__init__(fitness)

    def run(self, population):
        super(ReplacePopulationDuplicates, self).run(population, None)    

    