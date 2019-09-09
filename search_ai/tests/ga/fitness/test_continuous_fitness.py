import unittest.mock as mock

from search_ai.tests.ga.fitness.dumb_continuous_fitness import DumbContinuousFitness
from search_ai.tests.ga.fitness.test_fitness import TestFitnesses


class TestContinuousFitness(TestFitnesses.TestFitness):
    
    def setUp(self):
        super(TestContinuousFitness, self).setUp()
        self.len_features = 5
        self.features_info = [
            mock.MagicMock() for _ in range(self.len_features)
        ]
        self.fitness = DumbContinuousFitness(self.features_info)
    
    def test_continuous_fitness_constructor(self):
        self.check_fitness_constructor(self.fitness, self.len_features)
        self.cmp_arrays(self.fitness.features_info, self.features_info)
        
        continuous_fitness = DumbContinuousFitness(
            self.features_info[0:1]
        )
        self.check_fitness_constructor(continuous_fitness, 1)
        self.cmp_arrays(
            continuous_fitness.features_info,
            self.features_info[0:1]
        )
        
        continuous_fitness = DumbContinuousFitness(
            self.features_info * 2
        )
        self.check_fitness_constructor(continuous_fitness, 10)
        self.cmp_arrays(
            continuous_fitness.features_info,
            self.features_info * 2
        )
    
    def test_continuous_fitness_constructor_exception(self):
        with self.assertRaises(Exception):
            DumbContinuousFitness()
    
    def test_continuous_fitness_new_blank_individual(self):
        with mock.patch(
                'search_ai.ga.fitness.continuous_fitness.ContinuousIndividual'
        ) as mocked_ind:
            ind = mocked_ind.return_value
            self.assertIs(self.fitness.new_blank_individual(), ind)
            mocked_ind.assert_called_once_with(
                self.features_info,
                False
            )
    
    def test_continuous_fitness_new_random_individual(self):
        with mock.patch(
                'search_ai.ga.fitness.continuous_fitness.ContinuousIndividual'
        ) as mocked_ind:
            ind = mocked_ind.return_value
            self.assertIs(self.fitness.new_random_individual(), ind)
            mocked_ind.assert_called_once_with(self.features_info, True)
