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

        self.fitness = DumbContinuousFitness(self.features_info)

    def test_continuous_fitness_constructor(self):
        self.check_fitness_constructor(self.fitness, self.len_features)
        self.cmp_arrays(self.fitness.features_info, self.features_info)

        continuous_fitness = DumbContinuousFitness(self.features_info[0:1])
        self.check_fitness_constructor(continuous_fitness, 1)

        continuous_fitness = DumbContinuousFitness(self.features_info * 2)
        self.check_fitness_constructor(continuous_fitness, 10)

    def test_continuous_fitness_constructor_exception(self):
        with self.assertRaises(Exception):
            DumbContinuousFitness()

    def test_continuous_fitness_new_blank_individual(self):
        ind1 = self.fitness.new_blank_individual()
        ind2 = ContinuousIndividual(self.features_info, False)
        self.cmp_continuous_individuals(ind1, ind2)

        ind1 = DumbContinuousFitness([ContinuousParameterInfo(), ContinuousParameterInfo()]).new_blank_individual()
        ind2 = ContinuousIndividual([ContinuousParameterInfo(), ContinuousParameterInfo()], False)
        self.cmp_continuous_individuals(ind1, ind2)
