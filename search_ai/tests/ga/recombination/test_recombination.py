import unittest
from unittest.mock import MagicMock

from search_ai.ga.individual.binary_individual import BinaryIndividual
from search_ai.tests.test_case_with_utils import TestCaseWithUtils

class TestRecombinations(object):

    class TestRecombination(TestCaseWithUtils):

        def setUp(self):
            self.len_features = 5
            self.number_of_children = 4

        def set_up_fitness(self, number_of_children, times):
            self.fitness = MagicMock()
            self.fitness.new_blank_individual.side_effect = [BinaryIndividual(self.len_features) for i in range(number_of_children)] * times
 
        def check_fitness_interface(self, fitness):
            self.assertTrue(hasattr(fitness, 'new_blank_individual'))

        def check_recombination_attributes(self, recombination, number_of_children):
           self.assertEqual(self.number_of_children, self.recombination.number_of_children) 
           self.check_fitness_interface(self.recombination.fitness)

        def test_recombination_number_of_children(self):
            self.assertEqual(self.recombination.number_of_children, self.number_of_children)

            self.recombination.number_of_children = 1
            self.assertEqual(self.recombination.number_of_children, 1)

            self.recombination.number_of_children = 10
            self.assertEqual(self.recombination.number_of_children, 10)

        def test_recombination_number_of_children_exception(self):
            with self.assertRaises(ValueError):
                self.recombination.number_of_children = -100
                self.recombination.number_of_children = 0
