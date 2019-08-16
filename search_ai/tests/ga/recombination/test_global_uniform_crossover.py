import unittest.mock as mock

from search_ai.ga.recombination.global_uniform_crossover import GlobalUniformCrossover
from search_ai.ga.individual.binary_individual import BinaryIndividual

from search_ai.tests.ga.recombination.test_recombination import TestRecombinations


class TestGlobalUniformCrossover(TestRecombinations.TestRecombination):

    def set_all_individuals_features(self, individuals, value):
        for ind in individuals:
            for i in range(len(ind.features)):
                ind.features[i] = value

    def setUp(self):
        super(TestGlobalUniformCrossover, self).setUp()
        self.recombination = GlobalUniformCrossover(self.fitness, self.number_of_children)

    def test_global_uniform_crossover_constructor(self):
        self.check_recombination_attributes(self.recombination, self.number_of_children)
        rec = GlobalUniformCrossover(self.fitness, 1)
        self.check_recombination_attributes(rec, 1)

    def test_recombination_constructor_exception(self):
        with self.assertRaises(Exception):
            GlobalUniformCrossover(None, 2)
            GlobalUniformCrossover(self.fitness, 0)

    def test_global_uniform_crossover_run(self):            
        children = self.recombination.run(self.parents)
        self.cmp_arrays(children, self.children, lambda x, y: x is y)
        self.assertEqual(self.fitness.new_blank_individual.call_count, self.number_of_children)
        self.assertEqual(self.fitness.new_blank_individual.call_args_list, [mock.call() for _ in range(self.number_of_children)])
        self._assert_child_and_parent_mock_calls(self.children, self.parents)

    def _assert_child_and_parent_mock_calls(self, children, parents):
        for child in children:
            child.len_features.assert_called_once_with()
            self.assertEqual(child.set_feature_at.call_count, self.len_features)

            for i in range(self.len_features):
                child.set_feature_at.assert_any_call(i, True)
                self._assert_only_one_parent_has_call_with_index_per_child(self.parents, i)

    def _assert_only_one_parent_has_call_with_index_per_child(self, parents, index):
        called = 0

        for parent in parents:
            for call in parent.get_feature_at.call_args_list:
                if call == mock.call(index):
                    called += 1

        self.assertEqual(called, self.number_of_children)
