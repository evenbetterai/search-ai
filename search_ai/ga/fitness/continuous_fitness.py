import random as rd

from search_ai.ga.fitness.fitness import Fitness
from search_ai.ga.individual.continuous_individual import ContinuousIndividual


class ContinuousFitness(Fitness):

    def __init__(self, len_features, features_info):
        super(ContinuousFitness, self).__init__(len_features)
        self._features_info = list(features_info)

    @property
    def features_info(self):
        return self._features_info

    def new_blank_individual(self):
        return ContinuousIndividual(self._len_features, self._features_info)

    def new_random_individual(self):
        ind = self.new_blank_individual()

        for i in range(len(ind.features)):
            ind.features[i] = rd.uniform(ind.features_info[i].min_value, ind.features_info[i].max_value)

        return ind
