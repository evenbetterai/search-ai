from abc import ABC, abstractmethod

from search_ai.utils.search import Search


class ReplaceDuplicates(ABC):

    @staticmethod
    def cmp_by_features(self, individual):
        return individual.features

    def __init__(self, replacer):
        self._replacer = replacer
        self._population = None

    @property
    def replacer(self):
        return self._replacer

    @replacer.setter
    def replacer(self, replacer):
        self._replacer = replacer

    @abstractmethod
    def run(self, **kwargs):
        pass
