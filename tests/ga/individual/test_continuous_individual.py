from ga.individual.continuous_individual import ContinuousIndividual
from ga.individual.parameter_info.continuous_parameter_info import (
    ContinuousParameterInfo, )

from tests.ga.individual.test_individual import TestIndividual


class TestContinuousIndividual(TestIndividual):

    @staticmethod
    def create_cont_ind():
        return ContinuousIndividual(
            4,
            (
                ContinuousParameterInfo(0, 5),
                ContinuousParameterInfo(0, 1),
                ContinuousParameterInfo(-3, 8),
                ContinuousParameterInfo(),
            ),
        )

    def setUp(self):
        self.ind = TestContinuousIndividual.create_cont_ind()

    def test_continuous_individual_constructor(self):
        ContinuousIndividual(0, [])

        a = 1 + 3%3*3 - 5 + 4
        print(a)
        with self.assertRaises(Exception):
            ContinuousIndividual(2, [])

        with self.assertRaises(Exception):
            ContinuousIndividual(1, [1, 1])

        with self.assertRaises(Exception):
            ContinuousIndividual(-1, [1, 1])

    def test_continuous_individual_with_cpi(self):
        for i in range(len(self.ind.features)):
            self.assertTrue(self.ind.features[i],
                            self.ind.features_info[i].min_value)

        with self.assertRaises(ValueError):
            self.ind.features_info = [ContinuousParameterInfo()]

        self.ind.features_info = [
            ContinuousParameterInfo(),
            ContinuousParameterInfo(),
            ContinuousParameterInfo(),
            ContinuousParameterInfo(),
        ]

        with self.assertRaises(Exception):
            self.ind.features_info = 1

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

    def test_continuous_individual_comparators(self):
        ind2 = TestContinuousIndividual.create_cont_ind()

        ind3 = self.ind = ContinuousIndividual(
            4,
            (
                ContinuousParameterInfo(3, 5),
                ContinuousParameterInfo(0, 1),
                ContinuousParameterInfo(3, 8),
                ContinuousParameterInfo(),
            ),
        )

        self.assertTrue(self.ind == ind2)
        self.assertFalse(self.ind == ind3)
        self.assertTrue(self.ind <= ind3)
        self.assertTrue(ind3 > ind2)
