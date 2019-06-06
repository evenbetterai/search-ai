import numpy as np

from ga.individual.continuous_individual import ContinuousIndividual
from ga.individual.parameter_info.continuous_parameter_info import ContinuousParameterInfo

from tests.ga.individual.test_individual import TestIndividuals


class TestContinuousIndividual(TestIndividuals.TestIndividual):

    @staticmethod
    def create_continuous_ind(features_info_array):
        return ContinuousIndividual(
            len(features_info_array), list(features_info_array)
        )

    def setUp(self):
        self.continuous_params_info_array_1 = [
            ContinuousParameterInfo(2),
            ContinuousParameterInfo(0, 1),
            ContinuousParameterInfo(-3, 8),
            ContinuousParameterInfo()
        ]
        self.continuous_params_info_array_2 = [
            ContinuousParameterInfo(7, 10),
            ContinuousParameterInfo(5),
            ContinuousParameterInfo(3, 4)
        ]
        self.init_values_continuous_params_info_array_1 = [2, 0, -3, 0]
        self.init_values_continuous_params_info_array_2 = [7, 5, 3]
        self.ind = TestContinuousIndividual.create_continuous_ind(
            self.continuous_params_info_array_1
        )

    def test_continuous_individual_constructor(self):
        # it is possible to create such individual
        ContinuousIndividual(0, [])

        self.ind = TestContinuousIndividual.create_continuous_ind(
            self.continuous_params_info_array_2
        )
        self.cmp_arrays(
            self.ind.features,
            np.array(self.init_values_continuous_params_info_array_2)
        )
        self.cmp_arrays(
            self.ind.features_info, self.continuous_params_info_array_2
        )

    def test_continuous_individual_constructor_exception(self):
        with self.assertRaises(Exception):
            ContinuousIndividual(2, [])
            ContinuousIndividual(1, [1, 1])
            ContinuousIndividual(-1, [1, 1])

    def test_continuous_individual_features(self):
        self.cmp_arrays(
            self.ind.features,
            self.init_values_continuous_params_info_array_1
        )

        self.ind.set_feature_at(0, 2)
        self.ind.set_feature_at(1, 1)
        self.ind.set_feature_at(2, 1)
        self.ind.set_feature_at(3, 100)
        self.cmp_arrays(self.ind.features, np.array([2, 1, 1, 100]))

        self.ind._features = self.init_values_continuous_params_info_array_2[
            1:]
        self.cmp_arrays(
            self.ind.features,
            np.array(
                self.init_values_continuous_params_info_array_2[1:]
            )
        )

    def test_continuous_individual_features_exception(self):
        with self.assertRaises(ValueError):
            self.ind.set_feature_at(0, -100)
            self.ind.set_feature_at(1, 1000)

    def test_continuous_individual_features_info(self):
        self.cmp_arrays(
            self.ind.features_info, self.continuous_params_info_array_1
        )

        self.ind.features_info[0].min_value = 1
        self.ind.features_info[2].max_value = 0
        self.continuous_params_info_array_1[
            0] = ContinuousParameterInfo(1)
        self.continuous_params_info_array_1[
            2] = ContinuousParameterInfo(-3, 0)
        self.cmp_arrays(
            self.ind.features_info, self.continuous_params_info_array_1
        )

    def test_continuous_individual_comparators(self):
        ind2 = TestContinuousIndividual.create_continuous_ind(
            self.continuous_params_info_array_1
        )
        self.continuous_params_info_array_1[
            2] = ContinuousParameterInfo(3, 8)
        ind3 = TestContinuousIndividual.create_continuous_ind(
            self.continuous_params_info_array_1
        )

        self.assertTrue(self.ind == ind2)
        self.assertFalse(self.ind == ind3)
        self.assertTrue(self.ind <= ind3)
        self.assertTrue(ind3 > ind2)
