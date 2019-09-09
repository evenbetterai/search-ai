import math
import random as rd

from search_ai.ga.fitness.fitness import Fitness
from search_ai.ga.individual.binary_individual import BinaryIndividual


class BinaryFitness(Fitness):
    
    def __init__(self, len_features):
        super(BinaryFitness, self).__init__(len_features)
    
    def new_blank_individual(self):
        return BinaryIndividual(self._len_features, False)
    
    def new_random_individual(self):
        return BinaryIndividual(self._len_features, True)
