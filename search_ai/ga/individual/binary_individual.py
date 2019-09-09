import random as rd

from search_ai.ga.individual.individual import Individual
from search_ai.utils.bitarray import BitArray


class BinaryIndividual(Individual):
    
    DEFAULT_VALUE = 0
    
    def __init__(self, len_features, randomize_features=True):
        super(BinaryIndividual,
              self).__init__(len_features,
                             randomize_features)
    
    def _init_features_array(self, len_features):
        self._features = BitArray(len_features)
    
    def _randomize_features(self):
        for i in range(len(self._features)):
            self._features[i] = rd.randint(0, 1)
    
    def _default_features(self):
        for i in range(len(self._features)):
            self._features[i] = BinaryIndividual.DEFAULT_VALUE
