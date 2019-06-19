from unittest.mock import MagicMock
from search_ai.ga.mutation.standard_binary_mutation import StandardBinaryMutation
from search_ai.utils.bitarray import BitArray
from search_ai.tests.ga.mutation.test_mutation import TestMutations


class TestStandardBinaryMutation(TestMutations.TestMutation):

    def setUp(self):
        self.mutation_prob = 0.2
        self.mutation = StandardBinaryMutation(self.mutation_prob)
        self.individual = MagicMock()
        self.individual.features = BitArray("01000")


    def test_mutation_mutate(self):
        feature_before_mutation = self.individual.features[0]
        self.mutation.mutate(self.individual, 0)
        self.assertEqual(self.individual.features[0], not feature_before_mutation)

        feature_before_mutation = self.individual.features[1]
        self.mutation.mutate(self.individual, 1)
        self.assertEqual(self.individual.features[1], not feature_before_mutation)
