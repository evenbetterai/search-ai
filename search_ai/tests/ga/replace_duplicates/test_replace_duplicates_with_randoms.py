import unittest.mock as mock

from search_ai.ga.replace_duplicates.replace_duplicates_with_randoms import ReplaceDuplicatesWithRandoms
from search_ai.tests.ga.test_case_with_population import TestCaseWithPopulation


class TestReplaceDuplicatesWithRandoms(TestCaseWithPopulation):

    def setUp(self):
        self.u = 10
        self.diff = 2
        self.population = [self._mock_individual([1]) for _ in range(self.u - self.diff)]
        self.population += [self._mock_individual([2]) for _ in range(self.diff)]
        self.children = [self._mock_individual([3]) for _ in range(self.u * 2 - self.diff * 3)]
        self.children += [self._mock_individual([2]) for _ in range(self.diff * 3)]

        self.new_children = [mock.MagicMock() for _ in range(self.diff * 3)]
        self.fitness = mock.MagicMock()
        self.fitness.new_random_individual.side_effect = self.new_children

        self.replace_duplicates = ReplaceDuplicatesWithRandoms(self.fitness)

    def test_replace_duplicates_with_randoms(self):
        self.replace_duplicates.run(self.population, self.children)
        self.assertEqual(self.fitness.new_random_individual.call_count, self.u)
        self.cmp_arrays(self.children[0:self.u], [self.random_ind] * self.u)

    def _mock_individual(self, return_value):
        ind = {}
        ind['feature_prop_mock'] = mock.PropertyMock(return_value=return_value)
        ind['obj'] = mock.MagicMock()
        ind['obj'].features = ind['feature_prop_mock']
        return ind
