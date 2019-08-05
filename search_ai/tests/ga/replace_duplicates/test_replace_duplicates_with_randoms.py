from unittest.mock import MagicMock

from search_ai.ga.replace_duplicates.replace_duplicates_with_randoms import ReplaceDuplicatesWithRandoms
from search_ai.tests.ga.test_case_with_population import TestCaseWithPopulation


class TestReplaceDuplicatesWithRandoms(TestCaseWithPopulation):

    def setUp(self):
        self.u = 10
        self.population = self.create_population(self.u)
        self.children = list(self.population[0:self.u]) + self.create_population(self.u, None, [list(map(lambda i: i+1, self.population[0].features)) for _ in range(self.u)])

        self.fitness = MagicMock()
        self.random_ind = self.create_population(1)[0]
        self.fitness.new_random_individual.return_value = self.random_ind

        self.replace_duplicates = ReplaceDuplicatesWithRandoms(self.fitness)

    def test_replace_duplicates_with_randoms(self):
        self.replace_duplicates.run(self.population, self.children)
        self.assertEqual(self.fitness.new_random_individual.call_count, self.u)
        self.cmp_arrays(self.children[0:self.u], [self.random_ind] * self.u)
