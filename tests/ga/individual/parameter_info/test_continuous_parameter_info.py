import unittest

from ga.individual.parameter_info.continuous_parameter_info import (
    ContinuousParameterInfo,
)


class TestContinuousParameterInfo(unittest.TestCase):

    def setUp(self):
        self.cpi = ContinuousParameterInfo(-5, 5)

    def test_continuous_parameter_info_constructor(self):
        par = ContinuousParameterInfo()
        self.assertEqual(par.min_value, 0)
        self.assertEqual(par.max_value, 100)

        par = ContinuousParameterInfo(0.1)
        self.assertAlmostEqual(par.min_value, 0.1)
        self.assertEqual(par.max_value, 100)

        par = ContinuousParameterInfo(3.004, 3.05)
        self.assertAlmostEqual(par.min_value, 3.004)
        self.assertAlmostEqual(par.max_value, 3.05)

    def test_continuous_parameter_info_constructor_exception(self):
        with self.assertRaises(ValueError):
            ContinuousParameterInfo(3, 2)
            ContinuousParameterInfo(1.5, 1.499998)
            ContinuousParameterInfo(101)

    def test_continuous_parameter_info_min_value(self):
        self.assertEqual(self.cpi.min_value, -5)
        self.cpi.min_value = 3
        self.assertEqual(self.cpi.min_value, 3)

    def test_continuous_parameter_info_min_value_exception(self):
        with self.assertRaises(ValueError):
            self.cpi.min_value = 6

    def test_continuous_parameter_info_max_value(self):
        self.assertEqual(self.cpi.max_value, 5)
        self.cpi.max_value = 0
        self.assertEqual(self.cpi.max_value, 0)

    def test_continuous_parameter_info_max_value_exception(self):
        with self.assertRaises(ValueError):
            self.cpi.max_value = -10


if __name__ == "__main__":
    unittest.main()
