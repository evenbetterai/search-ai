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
