from collections import Sequence
from search_ai.utils.bitarray import BitArray

from search_ai.ga.individual.binary_individual import BinaryIndividual
from search_ai.tests.ga.individual.test_individual import TestIndividuals


class TestBinaryIndividual(TestIndividuals.TestIndividual):
    FEATURES_LEN = 5
    BIT_ARRAY_1 = BitArray("00000")
    BIT_ARRAY_2 = BitArray("10101")

    def __init__(self, *args, **kwargs):
        self.ind = None
        return super().__init__(*args, **kwargs)

    def setUp(self):
        self.ind = BinaryIndividual(5)

    def test_binary_individual_constructor(self):
        self.cmp_arrays(
            self.ind.features,
            TestBinaryIndividual.FEATURES_LEN * BitArray("0"),
            self.cmp_array_els
        )

    def test_binary_individual_constructor_exception(self):
        with self.assertRaises(Exception):
            BinaryIndividual(3.1)

        with self.assertRaises(Exception):
            BinaryIndividual([])

        with self.assertRaises(ValueError):
            BinaryIndividual(-1)

    def test_binary_individual_features(self):
        self.cmp_arrays(
            self.ind.features, TestBinaryIndividual.BIT_ARRAY_1, self.cmp_array_els
        )

        self.ind.set_feature_at(2, 1.2)
        self.ind.set_feature_at(0, True)
        self.ind.set_feature_at(4, 100)
        self.cmp_arrays(
            self.ind.features, TestBinaryIndividual.BIT_ARRAY_2, self.cmp_array_els
        )

    def test_binary_individual_comparators(self):
        ind1 = BinaryIndividual(TestBinaryIndividual.FEATURES_LEN)
        ind2 = BinaryIndividual(TestBinaryIndividual.FEATURES_LEN)
        ind3 = BinaryIndividual(TestBinaryIndividual.FEATURES_LEN)
        ind1.fitness = 0
        ind2.fitness = 0.1
        ind3.fitness = 0.89

        self.check_individual_comparators(ind1, ind2, ind3)

    def cmp_array_els(self, el1, el2):
        return bool(el1) == bool(el2)
