import unittest.mock as mock

from search_ai.ga.replace_duplicates.replace_children_duplicates_with_randoms import ReplaceChildrenDuplicatesWithRandoms
from search_ai.tests.ga.replace_duplicates.test_replace_duplicates import TestReplaceDuplicatesWrapper


class TestChildrenReplaceDuplicatesWithRandoms(TestReplaceDuplicatesWrapper.TestReplaceDuplicates):
    
    def setUp(self):
        super(TestReplaceDuplicatesWithRandoms, self).setUp()
        self.u = 10
        self.l = self.u * 3
        self.diff = 2
        self.population = [mock.MagicMock() for _ in range(self.u)]
        self.children = [mock.MagicMock() for _ in range(self.l)]
        self.old_children = list(self.children)
        self.new_children = [mock.MagicMock() for _ in range(self.diff)]

        self.fitness.new_random_individual.side_effect = self.new_children
        self.fitness.run.return_value = None

        self.replace_duplicates = ReplaceDuplicatesWithRandoms(self.fitness)

    def test_replace_duplicates_with_randoms(self):
        with mock.patch('search_ai.ga.replace_duplicates.replace_duplicates.Search') as mock_search:
            mock_search.sequencial_search.side_effect=[-1 for _ in range(self.l - self.diff)] + [i for i in range(self.diff)]
            self.replace_duplicates.run(self.population, self.children)
            self.assertEqual(mock_search.sequencial_search.call_count, len(self.old_children))
            self.assertEqual(self.fitness.new_random_individual.call_args_list, [mock.call() for i in range(self.diff)])
            self.assertEqual(self.fitness.run.call_args_list, [mock.call(self.new_children[i]) for i in range(self.diff)])

            for i in range(len(self.new_children)):
                self.assertIs(self.new_children[i], self.children[len(self.new_children) - 1 - i])

            for child in self.old_children:
                mock_search.sequencial_search.assert_any_call(self.population, child, mock.ANY)
