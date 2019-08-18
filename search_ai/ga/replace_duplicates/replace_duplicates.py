from abc import ABC, abstractmethod

from search_ai.utils.search import Search


class ReplaceDuplicates(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def replace_child(self, population, index):
        pass

    def run(self, population, children):
        for child in children:
            population_index = Search.sequencial_search(population, child, lambda ind: ind.features)

            if population_index >= 0:
                self.replace_child(population, population_index)
