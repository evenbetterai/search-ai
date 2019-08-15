import unittest.mock as mock

from search_ai.ga.individual.continuous_individual import ContinuousIndividual
from search_ai.ga.individual.feature_info.continuous_feature_info import ContinuousFeatureInfo

from search_ai.tests.ga.individual.test_individual import TestIndividuals


class TestContinuousIndividual(TestIndividuals.TestIndividual):

    def setUp(self):
        self.continuous_params_info_array_1 = [
            self._create_continuous_feature_info_mock(2),
            self._create_continuous_feature_info_mock(0, 1),
            self._create_continuous_feature_info_mock(-3, 8),
            self._create_continuous_feature_info_mock()
        ]

        self.continuous_params_info_array_2 = [
            self._create_continuous_feature_info_mock(7, 10),
            self._create_continuous_feature_info_mock(5),
            self._create_continuous_feature_info_mock(3, 4)
        ]
        
        self.continuous_params_info_array_3 = [
            self._create_continuous_feature_info_mock(7, 10),
            self._create_continuous_feature_info_mock(3, 4)
        ]

        self.init_values_continuous_params_info_array_1 = [2, 0, -3, 0]
        self.init_values_continuous_params_info_array_2 = [7, 5, 3]
        self.ind = self._create_continuous_ind(
            self.continuous_params_info_array_1
        )

    def test_continuous_individual_constructor(self):
        # it is possible to create such individual
        ContinuousIndividual([])

        self.cmp_arrays(self.ind._features, self.init_values_continuous_params_info_array_1)
        self.cmp_arrays(self.ind._features_info, self.continuous_params_info_array_1, lambda x, y: x is y['obj'])
        self._check_cfi_props_called_n_times(self.continuous_params_info_array_1, 1, 0)

        ind = self._create_continuous_ind(self.continuous_params_info_array_2, False)
        self.cmp_arrays(ind._features, self.init_values_continuous_params_info_array_2)
        self.cmp_arrays(ind._features_info, self.continuous_params_info_array_2, lambda x, y: x is y['obj'])
        self._check_cfi_props_called_n_times(self.continuous_params_info_array_2, 1, 0)

        ind = self._create_continuous_ind(self.continuous_params_info_array_3, True)
        self._random_features(ind)

    def test_continuous_individual_constructor_exception(self):
        with self.assertRaises(Exception):
            ContinuousIndividual(2, [])
            ContinuousIndividual(1, [1, 1])
            ContinuousIndividual(-1, [1, 1])

    def test_continuous_individual_set_feature_at(self):
        self.ind.set_feature_at(0, 2.2)
        self.assertEqual(self.ind._features[0], 2.2)
        self._check_cfi_props_called_n_times([self.continuous_params_info_array_1[0]], 2, 1)

        self.ind.set_feature_at(1, 0.43)
        self.assertEqual(self.ind._features[1], 0.43)
        self._check_cfi_props_called_n_times([self.continuous_params_info_array_1[1]], 2, 1)

        self.ind.set_feature_at(2, -2.2)
        self.assertEqual(self.ind._features[2], -2.2)
        self._check_cfi_props_called_n_times([self.continuous_params_info_array_1[2]], 2, 1)

        self.assertEqual(self.ind._features[3], 0)
        self._check_cfi_props_called_n_times([self.continuous_params_info_array_1[3]], 1, 0)

        self.ind.set_feature_at(-4, 99.9)
        self.assertEqual(self.ind._features[0], 99.9)
        self._check_cfi_props_called_n_times([self.continuous_params_info_array_1[0]], 3, 2)

        self.ind.set_feature_at(-3, 0.89)
        self.assertEqual(self.ind._features[1], 0.89)
        self._check_cfi_props_called_n_times([self.continuous_params_info_array_1[1]], 3, 2)

        self.ind.set_feature_at(-2, 4.5)
        self.assertEqual(self.ind._features[2], 4.5)
        self._check_cfi_props_called_n_times([self.continuous_params_info_array_1[2]], 3, 2)

        self.ind.set_feature_at(-1, 0.1)
        self.assertEqual(self.ind._features[3], 0.1)
        self._check_cfi_props_called_n_times([self.continuous_params_info_array_1[3]], 2, 1)

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
        cfi_mock = self._create_continuous_feature_info_mock(-1.3, 29.23)['obj']
        self.ind.set_feature_info_at(0, cfi_mock)
        self.assertEqual(self.ind._features_info[0], cfi_mock)

        self.ind.set_feature_info_at(1, cfi_mock)
        self.assertEqual(self.ind._features_info[1], cfi_mock)

        self.ind.set_feature_info_at(2, cfi_mock)
        self.assertEqual(self.ind._features_info[2], cfi_mock)

        self.assertEqual(self.ind._features_info[3], self.continuous_params_info_array_1[3]['obj'])

        self.ind.set_feature_info_at(-4, cfi_mock)
        self.assertEqual(self.ind._features_info[0], cfi_mock)

        self.ind.set_feature_info_at(-3, cfi_mock)
        self.assertEqual(self.ind._features_info[1], cfi_mock)

        self.ind.set_feature_info_at(-2, cfi_mock)
        self.assertEqual(self.ind._features_info[2], cfi_mock)

        self.ind.set_feature_info_at(-1, cfi_mock)
        self.assertEqual(self.ind._features_info[3], cfi_mock)

    def test_continuous_individual_set_feature_info_at_exception(self):
        cfi_mock = self._create_continuous_feature_info_mock(-100.3, -29.23)['obj']

        with self.assertRaises(Exception):
            self.ind.set_feature_info_at(-5, cfi_mock)
            self.ind.set_feature_info_at(4, cfi_mock)
            self.ind.set_feature_info_at(100, cfi_mock)

    def test_continuous_individual_get_feature_info_at(self):
        cfi_mock_1 =  self._create_continuous_feature_info_mock(0.2, 1.31)['obj']
        cfi_mock_2 =  self._create_continuous_feature_info_mock(2.234, 11.41)['obj']
        self.ind.set_feature_info_at(0, cfi_mock_1)
        self.ind.set_feature_info_at(2, cfi_mock_2)

        self.assertEqual(self.ind.get_feature_info_at(0), cfi_mock_1)
        self.assertEqual(self.ind.get_feature_info_at(-4), cfi_mock_1)
        self.assertEqual(self.ind.get_feature_info_at(1), self.continuous_params_info_array_1[1]['obj'])
        self.assertEqual(self.ind.get_feature_info_at(-3), self.continuous_params_info_array_1[1]['obj'])
        self.assertEqual(self.ind.get_feature_info_at(2), cfi_mock_2)
        self.assertEqual(self.ind.get_feature_info_at(-2), cfi_mock_2)
        self.assertEqual(self.ind.get_feature_info_at(3), self.continuous_params_info_array_1[3]['obj'])
        self.assertEqual(self.ind.get_feature_info_at(-1), self.continuous_params_info_array_1[3]['obj'])
        
    def test_continuous_individual_get_feature_info_at_exception(self):
        with self.assertRaises(Exception):
            self.ind.get_feature_info_at(-5)
            self.ind.get_feature_info_at(4)
            self.ind.get_feature_info_at(-1000)

    def test_continuous_individual_comparators(self):
        ind1 = self._create_continuous_ind(
            self.continuous_params_info_array_1
        )
        ind2 = self._create_continuous_ind(
            self.continuous_params_info_array_1
        )
        ind3 = self._create_continuous_ind(
            self.continuous_params_info_array_1
        )

        ind1.fitness = 0.1
        ind2.fitness = 0.11
        ind3.fitness = 0.12

        self.check_individual_comparators(ind1, ind2, ind3)


    def _create_continuous_ind(self, features_info_dict_list, random=False):
        features_info_array = [features_info_dict['obj'] for features_info_dict in features_info_dict_list]
        return ContinuousIndividual(list(features_info_array), random)

    def _create_continuous_feature_info_mock(self, min_value=0, max_value=100):
        cfi = {}
        cfi['min_value_prop_mock'] = mock.PropertyMock(return_value=min_value)
        cfi['max_value_prop_mock'] = mock.PropertyMock(return_value=max_value)
        cfi['obj'] = mock.MagicMock()
        type(cfi['obj']).min_value = cfi['min_value_prop_mock']
        type(cfi['obj']).max_value = cfi['max_value_prop_mock']
        return cfi

    def _random_features(self, ind):
        for i in range(ind.len_features):
            self.assertTrue(ind.get_feature_at(i) >= ind.get_feature_info_at(i).min_value and ind.get_feature_at(i) <= ind.get_feature_info_at(i).max_value)

    def _check_cfi_props_called_n_times(self, cfi_mock_list, min_prop_times, max_prop_times):
        for cfi_dict in cfi_mock_list:
            self.assertEqual(cfi_dict['min_value_prop_mock'].call_count, min_prop_times)
            self.assertEqual(cfi_dict['min_value_prop_mock'].mock_calls, [mock.call() for _ in range(min_prop_times)])
            self.assertEqual(cfi_dict['max_value_prop_mock'].call_count, max_prop_times)
            self.assertEqual(cfi_dict['max_value_prop_mock'].mock_calls, [mock.call() for _ in range(max_prop_times)])
