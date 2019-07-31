from unittest.mock import patch

from search_ai.ga.individual.binary_individual import BinaryIndividual
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
        ind1 = self.fitness.new_blank_individual()
        ind2 = BinaryIndividual(self.len_features)
        self.cmp_binary_individuals(ind1, ind2)

        ind1 = DumbBinaryFitness(2).new_blank_individual()
        ind2 = BinaryIndividual(2)
        self.cmp_binary_individuals(ind1, ind2)
