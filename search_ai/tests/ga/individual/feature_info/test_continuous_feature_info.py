import unittest

from search_ai.ga.individual.feature_info.continuous_feature_info import (
    ContinuousFeatureInfo,
)


class TestContinuousFeatureInfo(unittest.TestCase):
    
    def setUp(self):
        self.cpi = ContinuousFeatureInfo(-5, 5)
    
    def test_continuous_feature_info_constructor(self):
        par = ContinuousFeatureInfo()
        self.assertEqual(par.min_value, 0)
        self.assertEqual(par.max_value, 100)
        
        par = ContinuousFeatureInfo(0.1)
        self.assertAlmostEqual(par.min_value, 0.1)
        self.assertEqual(par.max_value, 100)
        
        par = ContinuousFeatureInfo(3.004, 3.05)
        self.assertAlmostEqual(par.min_value, 3.004)
        self.assertAlmostEqual(par.max_value, 3.05)
    
    def test_continuous_feature_info_constructor_exception(self):
        with self.assertRaises(ValueError):
            ContinuousFeatureInfo(3, 2)
            ContinuousFeatureInfo(1.5, 1.499998)
            ContinuousFeatureInfo(101)
    
    def test_continuous_feature_info_min_value(self):
        self.assertEqual(self.cpi.min_value, -5)
        self.cpi.min_value = 3
        self.assertEqual(self.cpi.min_value, 3)
    
    def test_continuous_feature_info_min_value_exception(self):
        with self.assertRaises(ValueError):
            self.cpi.min_value = 6
    
    def test_continuous_feature_info_max_value(self):
        self.assertEqual(self.cpi.max_value, 5)
        self.cpi.max_value = 0
        self.assertEqual(self.cpi.max_value, 0)
    
    def test_continuous_feature_info_max_value_exception(self):
        with self.assertRaises(ValueError):
            self.cpi.max_value = -10
