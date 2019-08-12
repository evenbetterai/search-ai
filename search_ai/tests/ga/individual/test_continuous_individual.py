import unittest.mock as mock

from search_ai.ga.individual.continuous_individual import ContinuousIndividual
from search_ai.ga.individual.feature_info.continuous_feature_info import ContinuousFeatureInfo

from search_ai.tests.ga.individual.test_individual import TestIndividuals


class TestContinuousIndividual(TestIndividuals.TestIndividual):

    def create_continuous_ind(self, features_info_array):
        return ContinuousIndividual(list(features_info_array), False)

    def create_continuous_feature_info_mock(self, min_value, max_value):
        cfi = object()
        cfi.min_value_prop_mock = mock.PropertyMock(return_value=min_value)
        cfi.max_value_prop_mock = mock.PropertyMock(return_value=max_value)
        cfi.obj = mock.MagicMock()
        type(cfi.obj).min_value = cfi.min_value_prop_mock
        type(cfi.obj).max_value = cfi.max_value_prop_mock

    def setUp(self):
        self.continuous_params_info_array_1 = [
            ContinuousFeatureInfo(2),
            ContinuousFeatureInfo(0, 1),
            ContinuousFeatureInfo(-3, 8),
            ContinuousFeatureInfo()
        ]
        self.continuous_params_info_array_2 = [
            ContinuousFeatureInfo(7, 10),
            ContinuousFeatureInfo(5),
            ContinuousFeatureInfo(3, 4)
        ]
        self.init_values_continuous_params_info_array_1 = [2, 0, -3, 0]
        self.init_values_continuous_params_info_array_2 = [7, 5, 3]
        self.ind = self.create_continuous_ind(
            self.continuous_params_info_array_1
        )

    def test_continuous_individual_constructor(self):
        # it is possible to create such individual
        ContinuousIndividual([])

        self.cmp_arrays(self.ind._features, self.init_values_continuous_params_info_array_1)
        self.cmp_arrays(self.ind._features_info, self.continuous_params_info_array_1)

        ind = self.create_continuous_ind(
            self.continuous_params_info_array_2
        )
        self.cmp_arrays(
            ind._features,
            self.init_values_continuous_params_info_array_2
        )
        self.cmp_arrays(
            ind._features_info, self.continuous_params_info_array_2
        )

        ind = ContinuousIndividual(self.continuous_params_info_array_1)
        self._random_features(ind)

    def test_continuous_individual_constructor_exception(self):
        with self.assertRaises(Exception):
            ContinuousIndividual(2, [])
            ContinuousIndividual(1, [1, 1])
            ContinuousIndividual(-1, [1, 1])

    def test_continuous_individual_set_feature_at(self):
        self.ind.set_feature_at(0, 2.2)
        self.assertEqual(self.ind._features[0], 2.2)

        self.ind.set_feature_at(1, 0.43)
        self.assertEqual(self.ind._features[1], 0.43)

        self.ind.set_feature_at(2, -2.2)
        self.assertEqual(self.ind._features[2], -2.2)

        self.assertEqual(self.ind._features[3], 0)

        self.ind.set_feature_at(-4, 99.9)
        self.assertEqual(self.ind._features[0], 99.9)

        self.ind.set_feature_at(-3, 0.89)
        self.assertEqual(self.ind._features[1], 0.89)

        self.ind.set_feature_at(-2, 4.5)
        self.assertEqual(self.ind._features[2], 4.5)

        self.ind.set_feature_at(-1, 0.1)
        self.assertEqual(self.ind._features[3], 0.1)

    def test_continuous_individual_set_feature_at_exception(self):
        with self.assertRaises(Exception):
            self.ind.set_feature_at(-5, True)
            self.ind.set_feature_at(4, False)
            self.ind.set_feature_at(100, False)

    def test_continuous_individual_get_feature_at(self):
        self.ind._features[0] = 35.57
        self.ind._features[2] = -0.58

        self.assertEqual(self.ind.get_feature_at(0), 35.57)
        self.assertEqual(self.ind.get_feature_at(-4), 35.57)
        self.assertEqual(self.ind.get_feature_at(1), 0)
        self.assertEqual(self.ind.get_feature_at(-3), 0)
        self.assertEqual(self.ind.get_feature_at(2), -0.58)
        self.assertEqual(self.ind.get_feature_at(-2), -0.58)
        self.assertEqual(self.ind.get_feature_at(3), 0)
        self.assertEqual(self.ind.get_feature_at(-1), 0)
        
    def test_continuous_individual_get_feature_at_exception(self):
        with self.assertRaises(Exception):
            self.ind.get_feature_at(-5)
            self.ind.get_feature_at(4)
            self.ind.get_feature_at(-1000)

    def test_continuous_individual_features_exception(self):
        with self.assertRaises(ValueError):
            self.ind.set_feature_at(0, -100)
            self.ind.set_feature_at(1, 1000)

    def test_continuous_individual_set_feature_info_at(self):
        self.ind.set_feature_info_at(0, ContinuousFeatureInfo(1, 3.2))
        self.assertEqual(self.ind._features_info[0], ContinuousFeatureInfo(1, 3.2))

        self.ind.set_feature_info_at(1, ContinuousFeatureInfo(1.1, 1.2))
        self.assertEqual(self.ind._features_info[1], ContinuousFeatureInfo(1.1, 1.2))

        self.ind.set_feature_info_at(2, ContinuousFeatureInfo(-2.3, -1))
        self.assertEqual(self.ind._features_info[2], ContinuousFeatureInfo(-2.3, -1))

        self.assertEqual(self.ind._features_info[3], ContinuousFeatureInfo(0, 100))

        self.ind.set_feature_info_at(-4, ContinuousFeatureInfo(1.4, 5))
        self.assertEqual(self.ind._features_info[0], ContinuousFeatureInfo(1.4, 5))

        self.ind.set_feature_info_at(-3, ContinuousFeatureInfo(-1.4, -0.1))
        self.assertEqual(self.ind._features_info[1], ContinuousFeatureInfo(-1.4, -0.1))

        self.ind.set_feature_info_at(-2, ContinuousFeatureInfo(14, 51))
        self.assertEqual(self.ind._features_info[2], ContinuousFeatureInfo(14, 51))

        self.ind.set_feature_info_at(-1, ContinuousFeatureInfo(14.2, 15))
        self.assertEqual(self.ind._features_info[3], ContinuousFeatureInfo(14.2, 15))

    def test_continuous_individual_set_feature_info_at_exception(self):
        with self.assertRaises(Exception):
            self.ind.set_feature_info_at(-5, ContinuousFeatureInfo())
            self.ind.set_feature_info_at(4, ContinuousFeatureInfo())
            self.ind.set_feature_info_at(100, ContinuousFeatureInfo())

    def test_continuous_individual_get_feature_info_at(self):
        self.ind.set_feature_info_at(0, ContinuousFeatureInfo(0.2, 1))
        self.ind.set_feature_info_at(2, ContinuousFeatureInfo(-14.2, -10))

        self.assertEqual(self.ind.get_feature_info_at(0), ContinuousFeatureInfo(0.2, 1))
        self.assertEqual(self.ind.get_feature_info_at(-4), ContinuousFeatureInfo(0.2, 1))
        self.assertEqual(self.ind.get_feature_info_at(1), ContinuousFeatureInfo(0, 1))
        self.assertEqual(self.ind.get_feature_info_at(-3), ContinuousFeatureInfo(0, 1))
        self.assertEqual(self.ind.get_feature_info_at(2), ContinuousFeatureInfo(-14.2, -10))
        self.assertEqual(self.ind.get_feature_info_at(-2), ContinuousFeatureInfo(-14.2, -10))
        self.assertEqual(self.ind.get_feature_info_at(3), ContinuousFeatureInfo(0, 100))
        self.assertEqual(self.ind.get_feature_info_at(-1), ContinuousFeatureInfo(0, 100))
        
    def test_continuous_individual_get_feature_info_at_exception(self):
        with self.assertRaises(Exception):
            self.ind.get_feature_info_at(-5)
            self.ind.get_feature_info_at(4)
            self.ind.get_feature_info_at(-1000)

    def test_continuous_individual_comparators(self):
        ind1 = self.create_continuous_ind(
            self.continuous_params_info_array_1
        )
        ind2 = self.create_continuous_ind(
            self.continuous_params_info_array_1
        )
        ind3 = self.create_continuous_ind(
            self.continuous_params_info_array_1
        )

        ind1.fitness = 0.1
        ind2.fitness = 0.11
        ind3.fitness = 0.12

        self.check_individual_comparators(ind1, ind2, ind3)

    def _random_features(self, ind):
        for i in range(len(ind.features)):
            self.assertTrue(ind.get_feature_at(i) >= ind.get_feature_info_at(i).min_value and ind.get_feature_at(i) <= ind.get_feature_info_at(i).max_value)
