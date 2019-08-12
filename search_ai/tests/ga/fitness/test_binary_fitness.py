import unittest.mock as mock

from search_ai.tests.ga.fitness.dumb_binary_fitness import DumbBinaryFitness
from search_ai.tests.ga.fitness.test_fitness import TestFitnesses


class TestBinaryFitness(TestFitnesses.TestFitness):

    def setUp(self):
        super(TestBinaryFitness, self).setUp()
        self.fitness = DumbBinaryFitness(self.len_features)

    def test_binary_fitness_constructor(self):
        self.check_fitness_constructor(self.fitness, self.len_features)

        binary_fitness = DumbBinaryFitness(1)
        self.check_fitness_constructor(binary_fitness, 1)

        binary_fitness = DumbBinaryFitness(10)
        self.check_fitness_constructor(binary_fitness, 10)

    def test_binary_fitness_constructor_exception(self):
        with self.assertRaises(ValueError):
            DumbBinaryFitness(0)
            DumbBinaryFitness(-2)

        with self.assertRaises(Exception):
            DumbBinaryFitness()

    def test_binary_fitness_new_blank_individual(self):
        with mock.patch('search_ai.ga.fitness.binary_fitness.BinaryIndividual') as mocked_ind:
            ind = mocked_ind.return_value
            self.assertIs(self.fitness.new_blank_individual(), ind)
            mocked_ind.assert_called_once_with(self.len_features, False)

    def test_binary_fitness_new_random_individual(self):
        with mock.patch('search_ai.ga.fitness.binary_fitness.BinaryIndividual') as mocked_ind:
            ind = mocked_ind.return_value
            self.assertIs(self.fitness.new_random_individual(), ind)
            mocked_ind.assert_called_once_with(self.len_features, True)
