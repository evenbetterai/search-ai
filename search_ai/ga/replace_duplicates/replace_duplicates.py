from abc import ABC, abstractmethod

from search_ai.utils.search import Search


class ReplaceDuplicates(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def replace_child(self, children, index):
        pass

    def run(self, population, children):
        for index in range(len(children) -1, -1, -1):
            if Search.sequencial_search(population, children[index], lambda ind: ind.features) > -1:
                self.replace_child(children, index)
