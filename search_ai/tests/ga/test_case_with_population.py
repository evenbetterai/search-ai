from unittest.mock import MagicMock

from search_ai.tests.test_case_with_utils import TestCaseWithUtils


class TestCaseWithPopulation(TestCaseWithUtils):

    def create_population(self, n, ind_mock=None, features=None, fitness=None):
        ind_mock, features, fitness = self._check_create_population_args(n, ind_mock, features, fitness)

        population = []
        for i in range(n):
            ind = ind_mock()
            ind.features = features[i]
            ind.fitness = fitness[i]
            population.append(ind)

        return population

    def _check_create_population_args(self, n, ind_mock, features, fitness):
        if ind_mock is None:
            ind_mock = self.default_ind_mock

        if features is None:
            features = self.default_features(n)

        if fitness is None:
            fitness = self.default_fitness(n)

        return ind_mock, features, fitness
        
    def default_ind_mock(self):
        mock = MagicMock()
        mock.__lt__ = lambda self, other: self.fitness < other.fitness
        mock.__eq__ = lambda self, other: self.fitness == other.fitness
        return mock

    def default_features(self, n):
        features = []
        for i in range(n):
            feature = [0 for _ in range(n)]
            feature[i] = 1
            features.append(feature)

        return features

    def default_fitness(self, n):
        return [i/n for i in range(n)]

    def _cmp_individuals(self, ind1, ind2):
        self.assertEqual(ind1.fitness, ind2.fitness)
        self.assertEqual(len(ind1.features), len(ind2.features))

        for i in range(len(ind1.features)):
            self.assertEqual(ind1.features[i], ind2.features[i])
    
    def _cmp_continuous_individuals_features_info(self, ind1, ind2):
        for i in range(len(ind1.features_info)):
            self.assertEqual(ind1.features_info[i].min_value, ind2.features_info[i].min_value)
            self.assertEqual(ind1.features_info[i].max_value, ind2.features_info[i].max_value)

    def cmp_binary_individuals(self, ind1, ind2):
        self._cmp_individuals(ind1, ind2)

    def cmp_continuous_individuals(self, ind1, ind2):
        self._cmp_individuals(ind1, ind2)
        self._cmp_continuous_individuals_features_info(ind1, ind2)
        
