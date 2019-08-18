import unittest.mock as mock

from search_ai.ga.replace_duplicates.replace_duplicates_with_randoms import ReplaceDuplicatesWithRandoms
from search_ai.tests.ga.test_case_with_population import TestCaseWithPopulation


class TestReplaceDuplicatesWithRandoms(TestCaseWithPopulation):

    def setUp(self):
        self.u = 10
        self.l = self.u * 3
        self.diff = 2
        self.population = [mock.MagicMock() for _ in range(self.u)]
        self.children = [mock.MagicMock() for _ in range(self.l)]
        self.new_children = [mock.MagicMock() for _ in range(self.diff)]

        self.fitness = mock.MagicMock()
        self.fitness.new_random_individual.side_effect = self.new_children

        self.replace_duplicates = ReplaceDuplicatesWithRandoms(self.fitness)

    def test_replace_duplicates_with_randoms(self):
        with mock.patch('search_ai.ga.replace_duplicates.replace_duplicates.Search') as mock_search:
            mock_search.sequencial_search.side_effect=[-1 for _ in range(self.l - self.diff)] + [i for i in range(self.diff)]
            self.replace_duplicates.run(self.population, self.children)
            self.assertEqual(self.fitness.new_random_individual.call_args_list, [mock.call() for _ in range(self.diff)])

            for new_child in self.new_children:
                self.assertIn(new_child, self.population)
