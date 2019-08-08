import random as rd

from search_ai.ga.fitness.fitness import Fitness
from search_ai.ga.individual.continuous_individual import ContinuousIndividual


class ContinuousFitness(Fitness):

    def __init__(self, features_info):
        super(ContinuousFitness, self).__init__(len(features_info))
        self._features_info = list(features_info)

    @property
    def features_info(self):
        return self._features_info

    def new_blank_individual(self):
        return ContinuousIndividual(self._features_info, False)

    def new_random_individual(self):
        return ContinuousIndividual(self._features_info)
