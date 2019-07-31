from unittest.mock import patch

from search_ai.ga.individual.parameter_info.continuous_parameter_info import ContinuousParameterInfo
from search_ai.ga.individual.continuous_individual import ContinuousIndividual
from search_ai.tests.ga.fitness.dumb_continuous_fitness import DumbContinuousFitness

from search_ai.tests.ga.fitness.test_fitness import TestFitnesses


class TestContinuousFitness(TestFitnesses.TestFitness):

    def setUp(self):
        super(TestContinuousFitness, self).setUp()
        self.len_features = 5
        self.features_info = [
            ContinuousParameterInfo(10, 15),
            ContinuousParameterInfo(20, 40),
            ContinuousParameterInfo(),
            ContinuousParameterInfo(0, 10),
            ContinuousParameterInfo(100, 1000),
        ]

        self.fitness = DumbContinuousFitness(self.len_features, self.features_info)

    def test_continuous_fitness_constructor(self):
        self.check_fitness_constructor(self.fitness, self.len_features)
        self.cmp_arrays(self.fitness.features_info, self.features_info)

        continuous_fitness = DumbContinuousFitness(1, self.features_info)
        self.check_fitness_constructor(continuous_fitness, 1)

        continuous_fitness = DumbContinuousFitness(10, self.features_info)
        self.check_fitness_constructor(continuous_fitness, 10)

    def test_continuous_fitness_constructor_exception(self):
        with self.assertRaises(ValueError):
            DumbContinuousFitness(0, self.features_info)
            DumbContinuousFitness(-2, self.features_info)

        with self.assertRaises(Exception):
            DumbContinuousFitness()

    def test_continuous_fitness_new_blank_individual(self):
        ind1 = self.fitness.new_blank_individual()
        ind2 = ContinuousIndividual(self.len_features, self.features_info)
        self.cmp_continuous_individuals(ind1, ind2)

        ind1 = DumbContinuousFitness(2, [ContinuousParameterInfo(), ContinuousParameterInfo()]).new_blank_individual()
        ind2 = ContinuousIndividual(2, [ContinuousParameterInfo(), ContinuousParameterInfo()])
        self.cmp_continuous_individuals(ind1, ind2)
