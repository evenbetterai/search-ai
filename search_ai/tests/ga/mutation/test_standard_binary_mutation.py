from unittest.mock import MagicMock
from search_ai.ga.mutation.standard_binary_mutation import StandardBinaryMutation
from search_ai.utils.bitarray import BitArray
from search_ai.tests.ga.mutation.test_mutation import TestMutations


class TestStandardBinaryMutation(TestMutations.TestMutation):

    def setUp(self):
        self.mutation_prob = 0.2
        self.mutation = StandardBinaryMutation(self.mutation_prob)
        self.individual = MagicMock()
        self.individual.features = [False, True, False, False, False]


    def test_mutation_mutate(self):
        feature_before_mutation = self.individual.features[0]
        self.mutation.mutate(self.individual, 0)
        self.assertEqual(self.individual.features[0], not feature_before_mutation)

        feature_before_mutation = self.individual.features[1]
        self.mutation.mutate(self.individual, 1)
        self.assertEqual(self.individual.features[1], not feature_before_mutation)

    def test_mutation_run(self):
        self.mutation.mutation_prob = 0
        features_before_mutation = list(self.individual.features)
        self.mutation.run(self.individual)
        self.cmp_arrays(self.individual.features, features_before_mutation)

        self.mutation.mutation_prob = 1
        features_before_mutation = [not feature for feature in self.individual.features]
        self.mutation.run(self.individual)
        self.cmp_arrays(self.individual.features, features_before_mutation)

        self.mutation.mutation_prob = 0.3
        self.mutation.run(self.individual)

        for feature in self.individual.features:
            self.assertTrue(feature == 0 or feature == 1)
