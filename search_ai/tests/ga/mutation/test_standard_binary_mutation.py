import unittest.mock as mock
from search_ai.ga.mutation.standard_binary_mutation import StandardBinaryMutation
from search_ai.utils.bitarray import BitArray
from search_ai.tests.ga.mutation.test_mutation import TestMutations


class TestStandardBinaryMutation(TestMutations.TestMutation):
    
    def setUp(self):
        self.mutation_prob = 0.2
        self.mutation = StandardBinaryMutation(self.mutation_prob)
        self.individual = mock.MagicMock()
        self.features = [False, True, False, False, False]
        self.individual.len_features.return_value = len(self.features)
        self.individual.get_feature_at.side_effect = self.features
        self.individual.set_feature_at.return_value = None
    
    def test_mutation_mutate(self):
        self.mutation.mutate(self.individual, 0)
        self.individual.get_feature_at.assert_called_once_with(0)
        self.individual.set_feature_at.assert_called_once_with(
            0,
            not self.features[0]
        )
        
        self.individual.reset_mock()
        self.mutation.mutate(self.individual, 1)
        self.individual.get_feature_at.assert_called_once_with(1)
        self.individual.set_feature_at.assert_called_once_with(
            1,
            not self.features[1]
        )
    
    def test_mutation_run_with_mutation_prob_at_0(self):
        self.mutation.mutation_prob = 0
        self.mutation.run(self.individual)
        self.individual.len_features.assert_called_once_with()
        self.individual.get_feature_at.assert_not_called()
        self.individual.set_feature_at.assert_not_called()
    
    def test_mutation_run_with_mutation_prob_at_1(self):
        self.mutation.mutation_prob = 1
        self.mutation.run(self.individual)
        self.individual.len_features.assert_called_once_with()
        self.assertEqual(
            self.individual.get_feature_at.call_count,
            len(self.features)
        )
        self.assertEqual(
            self.individual.set_feature_at.call_count,
            len(self.features)
        )
        self.individual.get_feature_at.assert_has_calls([
            mock.call(i) for i in range(len(self.features))
        ])
        self.individual.set_feature_at.assert_has_calls([
            mock.call(i,
                      not self.features[i])
            for i in range(len(self.features))
        ])
    
    def test_mutation_run_with_mutation_prob_between_0_and_1(self):
        self.mutation.mutation_prob = self.mutation_prob
        self.mutation.run(self.individual)
        self.individual.len_features.assert_called_once_with()
        self.assertGreaterEqual(
            self.individual.get_feature_at.call_count,
            0
        )
        self.assertGreaterEqual(
            self.individual.set_feature_at.call_count,
            0
        )
        self.assertLessEqual(
            self.individual.get_feature_at.call_count,
            len(self.features)
        )
        self.assertLessEqual(
            self.individual.set_feature_at.call_count,
            len(self.features)
        )
