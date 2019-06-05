from collections import Sequence
from utils.bitarray import BitArray

from ga.individual.binary_individual import BinaryIndividual
from tests.ga.individual.test_individual import TestIndividual


class TestBinaryIndividual(TestIndividual):
    FEATURES_LEN = 4
    BIT_ARRAY_1 = BitArray("00000")
    BIT_ARRAY_2 = BitArray("10101")

    def setUp(self):
        self.ind = BinaryIndividual(5)

    def test_binary_individual_constructor(self):
        ind = BinaryIndividual(FEATURES_LEN)
        self.check_new_individual(ind, BitArray(FEATURES_LEN))

    def test_binary_individual_constructor_exception(self):
        with self.assertRaises(Exception):
            BinaryIndividual(3.1)

        with self.assertRaises(Exception):
            BinaryIndividual([])

        with self.assertRaises(Exception):
            BinaryIndividual(-1)

    def test_binary_individual_features(self):
        self.cmp_arrays(self.ind.features, BIT_ARRAY_1)

        self.ind.set_feature_at(2, 1.2)
        self.ind.set_feature_at(0, True)
        self.ind.set_feature_at(4, 100)
        self.cmp_arrays(self.ind.features, BIT_ARRAY_2)

    def test_binary_individual_comparators(self):
        ind1 = BinaryIndividual(FEATURES_LEN)
        ind2 = BinaryIndividual(FEATURES_LEN)
        ind1._features = BitArray("0100")
        ind2._features = BitArray("0110")
        self.ind.features[1] = 1

        self.assertTrue(self.ind == ind1)
        self.assertFalse(self.ind == ind2)
        self.assertTrue(self.ind <= ind2)
        self.assertTrue(self.ind <= ind1)
        self.assertTrue(ind2 > ind1)

    def cmp_array_els(self, el1, el2):
        self.assertEqual(bool(el1), bool(el2))
