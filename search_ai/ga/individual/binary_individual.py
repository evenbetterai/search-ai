from search_ai.ga.individual.individual import Individual
from search_ai.utils.bitarray import BitArray


class BinaryIndividual(Individual):

    def __init__(self, len_features):
        super(BinaryIndividual, self).__init__(len_features)

    def _init_features(self, len_features):
        if len_features < 0:
            raise ValueError(
                "'len_features' parameter should not be negative"
            )

        self._features = len_features * BitArray("0")
