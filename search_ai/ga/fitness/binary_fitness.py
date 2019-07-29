import math
import random as rd

from search_ai.ga.fitness.fitness import Fitness
from search_ai.ga.individual.binary_individual import BinaryIndividual


class BinaryFitness(Fitness):

    def __init__(self, len_features):
        super(BinaryFitness, self).__init__(len_features)

    def new_blank_individual(self):
        return BinaryIndividual(self._len_features)

    def new_random_individual(self):
        ind = self.new_blank_individual()

        for i in range(len(ind.features)):
            ind.features[i] = rd.randint(0, 1)

        return ind
