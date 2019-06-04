from collections import Sequence
from utils.bitarray import BitArray

from ga.individual.binary_individual import BinaryIndividual
from tests.ga.individual.test_individual import TestIndividual


class TestBinaryIndividual(TestIndividual):
    def setUp(self):
        self.ind = BinaryIndividual(5)

    def test_binary_individual_constructor(self):
        with self.assertRaises(Exception):
            BinaryIndividual(3.1)

        with self.assertRaises(Exception):
            BinaryIndividual([])

        with self.assertRaises(Exception):
            BinaryIndividual(-1)

    def test_binary_individual_features(self):
        self.assertTrue(isinstance(self.ind.features, Sequence))
        self.assertEqual(len(self.ind.features), 5)
        self.check_individual_features(BitArray("00000"))

        self.ind.set_feature_at(2, 1)
        self.ind.set_feature_at(0, True)
        self.ind.set_feature_at(4, 100)
        self.check_individual_features(BitArray("10101"))

        self.ind._features = BitArray("0110")
        self.check_individual_features(BitArray([0, 100, True, 0]))

    def check_individual_features(self, array):
        self.assertEqual(len(self.ind.features), len(array))

        for i in range(len(self.ind.features)):
            self.assertEqual(bool(self.ind.features[i]), bool(array[i]))

    def test_binary_individual_comparators(self):
        ind2 = BinaryIndividual(5)
        ind3 = BinaryIndividual(5)
        ind2._features = BitArray("01000")
        ind3._features = BitArray("01100")
        self.ind.features[1] = 1

        self.assertTrue(self.ind == ind2)
        self.assertFalse(self.ind == ind3)
        self.assertTrue(self.ind <= ind3)
        self.assertTrue(self.ind <= ind2)
        self.assertTrue(ind3 > ind2)
