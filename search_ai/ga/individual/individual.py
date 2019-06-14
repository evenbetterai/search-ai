from abc import ABC, abstractmethod
import functools as ft


@ft.total_ordering
class Individual(ABC):
    """
    Class to represent a gentic individual. This individual has features
    (genes) that can be continuous or binary. The objective is to
    optimize all individual's features to get the best fitness value
    possible.
    """

    __slots__ = ["_age", "_features", "_fitness"]

    def __init__(self, len_features):
        self._age = 0
        self._features = None
        self._fitness = 0

        if len_features < 0:
            raise ValueError(
                "'len_features' should be greater or equal to '0'"
            )

        self._init_features(len_features)

    def __eq__(self, other):
        return self._fitness == other.fitness

    def __lt__(self, other):
        return self._fitness < other.fitness

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if new_age < 0:
            raise ValueError(
                "'new_age' has to hold a " +
                "number greater or equal to '0'"
            )

        self._age = new_age

    @property
    def fitness(self):
        return self._fitness

    @fitness.setter
    def fitness(self, fitness):
        if fitness < 0 or fitness > 1:
            raise ValueError(
                "'fitness' parameter has to hold a value between 0 and 1"
            )

        self._fitness = fitness

    @property
    def features(self):
        return self._features

    def get_feature_at(self, index):
        return self._features[index]

    def set_feature_at(self, index, new_value):
        self._features[index] = new_value

    @abstractmethod
    def _init_features(self, len_features):
        pass
