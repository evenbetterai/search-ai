from ga.individual.continuous_individual import ContinuousIndividual
from ga.individual.parameter_info.continuous_parameter_info import (
    ContinuousParameterInfo, )

from tests.ga.individual.test_individual import TestIndividual


class TestContinuousIndividual(TestIndividuals.TestIndividual):

    features_len = 4
    param_info_min1 = 1
    param_info_min2 = 0
    continuous_params_info_array_1 = (ContinuousParameterInfo(param_info_min1, 2), ContinuousParameterInfo(param_info_min2))
    continuous_params_info_array_2 = (ContinuousParameterInfo(param_info_min1, 2), ContinuousParameterInfo(param_info_min2), ContinuousParameterInfo(), ContinuousParameterInfo())
    continuous_params_info_array_3 = (ContinuousParameterInfo(0, 5), ContinuousParameterInfo(0, 1), ContinuousParameterInfo(-3, 8), ContinuousParameterInfo())
    init_values_continuous_params_info_array_3 = [0, 0, -3, 0]

    @staticmethod
    def create_cont_ind(features_info_array):
        return ContinuousIndividual(
            len(features_info_array),
            list(features_info_array)
        )

    def setUp(self):
        self.continuous_params_info_array = (ContinuousParameterInfo(0, 5), ContinuousParameterInfo(0, 1), ContinuousParameterInfo(-3, 8), ContinuousParameterInfo())
        self.ind = TestContinuousIndividual.create_cont_ind(self.continuous_params_info_array)

    def test_continuous_individual_constructor(self):
        # is possible to create such individual
        ContinuousIndividual(0, [])
        ind = ContinuousIndividual(2, continuous_params_info_array_1)
        self.check_new_individual(ind, [param_info_min1, param_info_min2])
        self.cmp_arrays(ind.features_info, continuous_params_info_array_1)

    def test_continuous_individual_constructor_exception(self):
        with self.assertRaises(Exception):
            ContinuousIndividual(2, [])

        with self.assertRaises(Exception):
            ContinuousIndividual(1, [1, 1])

        with self.assertRaises(Exception):
            ContinuousIndividual(-1, [1, 1])

    def test_continuous_individual_features_info(self):
        self.cmp_arrays(self.ind.features_info, self.continuous_params_info_array)

        self.ind.features_info[0].min_value = 1
        self.ind.features_info[2].max_value = 0
        self.continuous_params_info_array[0] = ContinuousParameterInfo(1,5)
        self.continuous_params_info_array[2] = ContinuousParameterInfo(-3, 0)
        self.cmp_arrays(self.ind._features, self.continuous_params_info_array)

        self.ind.features_info = continuous_params_info_array_2
        self.cmp_arrays(self.ind.features_info, continuous_params_info_array_2)

    def test_continuous_individual_features_info_exception(self):
        with self.assertRaises(ValueError):
            self.ind.features_info = self.continuous_params_info_array[1:]

        with self.assertRaises(Exception):
            self.ind.features_info = 1

    def test_continuous_individual_features(self):
        self.cmp_arrays(self.ind.features, self.continuous_params_info_array)

        self.ind.set_feature_at(0, 2)
        self.ind.set_feature_at(1, 1)
        self.ind.set_feature_at(2, 1)
        self.ind.set_feature_at(3, 100)
        self.cmp_arrays(self.inf.features, [2, 1, 1, 100])

        self.ind._features = self.continuous_params_info_array[1:]
        self.check_individual_features(self.continuous_params_info_array[1:])

    def test_continuous_individual_features_exception(self):
        with self.assertRaises(ValueError):
            self.ind.set_feature_at(0, -100)
            self.ind.set_feature_at(1, 1000)

    def test_continuous_individual_comparators(self):
        ind2 = TestContinuousIndividual.create_cont_ind(self.continuous_params_info_array)
        self.continuous_params_info_array[2] = ContinuousParameterInfo(3, 8)
        ind3 = TestContinuousIndividual.create_cont_ind(self.continuous_params_info_array)

        self.assertTrue(self.ind == ind2)
        self.assertFalse(self.ind == ind3)
        self.assertTrue(self.ind <= ind3)
        self.assertTrue(ind3 > ind2)
