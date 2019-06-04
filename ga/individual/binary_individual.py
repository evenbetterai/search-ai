from ga.individual.individual import Individual
from utils.bitarray import BitArray


class BinaryIndividual(Individual):
    def __init__(self, len_features):
        super(BinaryIndividual, self).__init__(len_features)

    def _init_features(self, len_features):
        self._features = len_features * BitArray("0")
