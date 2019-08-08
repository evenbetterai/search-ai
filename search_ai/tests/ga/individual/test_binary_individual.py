from collections import Sequence
from search_ai.utils.bitarray import BitArray

from search_ai.ga.individual.binary_individual import BinaryIndividual
from search_ai.tests.ga.individual.test_individual import TestIndividuals


class TestBinaryIndividual(TestIndividuals.TestIndividual):

    def setUp(self):
        super(TestBinaryIndividual, self).setUp()
        self.features_len = 5
        self.bit_array_1 = BitArray("00000")
        self.bit_array_2 = BitArray("10101")
        self.ind = BinaryIndividual(5, False)

    def test_binary_individual_constructor(self):
        self.cmp_arrays(self.ind.features, self.bit_array_1, self.cmp_array_els)

        ind = BinaryIndividual(7, True)
        self._random_features(ind)

    def test_binary_individual_constructor_exception(self):
        with self.assertRaises(Exception):
            BinaryIndividual(3.1)

        with self.assertRaises(Exception):
            BinaryIndividual([])

        with self.assertRaises(ValueError):
            BinaryIndividual(-1)

    def test_binary_individual_set_feature_at(self):
        self.ind.set_feature_at(0, 1.2)
        self.assertEqual(self.ind._features[0], True)

        self.ind.set_feature_at(1, True)
        self.assertEqual(self.ind._features[1], True)

        self.ind.set_feature_at(2, 100)
        self.assertEqual(self.ind._features[2], True)

        self.assertEqual(self.ind._features[3], False)
        self.assertEqual(self.ind._features[4], False)

        self.ind.set_feature_at(-5, False)
        self.assertEqual(self.ind._features[0], False)

        self.ind.set_feature_at(-4, False)
        self.assertEqual(self.ind._features[1], False)

        self.ind.set_feature_at(-3, False)
        self.assertEqual(self.ind._features[2], False)

        self.ind.set_feature_at(-2, 1)
        self.assertEqual(self.ind._features[3], True)

        self.ind.set_feature_at(-1, True)
        self.assertEqual(self.ind._features[4], True)

    def test_binary_individual_set_feature_at_exception(self):
        with self.assertRaises(Exception):
            self.ind.set_feature_at(-6, True)
            self.ind.set_feature_at(5, False)
            self.ind.set_feature_at(100, False)

    def test_binary_individual_get_feature_at(self):
        self.ind.set_feature_at(0, 1)
        self.ind.set_feature_at(2, True)
        self.ind.set_feature_at(4, 3.1)

        self.assertEqual(self.ind.get_feature_at(0), True)
        self.assertEqual(self.ind.get_feature_at(-5), True)
        self.assertEqual(self.ind.get_feature_at(1), False)
        self.assertEqual(self.ind.get_feature_at(-4), False)
        self.assertEqual(self.ind.get_feature_at(2), True)
        self.assertEqual(self.ind.get_feature_at(-3), True)
        self.assertEqual(self.ind.get_feature_at(3), False)
        self.assertEqual(self.ind.get_feature_at(-2), False)
        self.assertEqual(self.ind.get_feature_at(4), True)
        self.assertEqual(self.ind.get_feature_at(-1), True)
        
    def test_binary_individual_get_feature_at_exception(self):
        with self.assertRaises(Exception):
            self.ind.get_feature_at(-6)
            self.ind.get_feature_at(5)
            self.ind.get_feature_at(-1000)

    def test_binary_individual_features(self):
        self.cmp_arrays(
            self.ind.features, self.bit_array_1, self.cmp_array_els
        )

        self.ind.set_feature_at(2, 1.2)
        self.ind.set_feature_at(0, True)
        self.ind.set_feature_at(4, 100)
        self.cmp_arrays(
            self.ind.features, self.bit_array_2, self.cmp_array_els
        )

    def test_binary_individual_comparators(self):
        ind1 = BinaryIndividual(self.features_len)
        ind2 = BinaryIndividual(self.features_len)
        ind3 = BinaryIndividual(self.features_len)
        ind1.fitness = 0
        ind2.fitness = 0.1
        ind3.fitness = 0.89

        self.check_individual_comparators(ind1, ind2, ind3)

    def cmp_array_els(self, el1, el2):
        return bool(el1) == bool(el2)

    def _random_features(self, ind):
        for i in range(len(ind.features)):
            self.assertTrue(ind.get_feature_at(i) == False or ind.get_feature_at(i) == True)
