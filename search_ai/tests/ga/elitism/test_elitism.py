import unittest


class TestElitisms(object):
    
    class TestElitism(unittest.TestCase):
        
        def setUp(self):
            self.k = 4
        
        def check_elitism_constructor(self, elitism, k):
            self.assertEqual(elitism.k, k)
        
        def test_elitism_k(self):
            self.assertEqual(self.elitism.k, self.k)
            
            self.elitism.k = 1
            self.assertEqual(self.elitism.k, 1)
            
            self.elitism.k = 111
            self.assertEqual(self.elitism.k, 111)
        
        def test_elitism_k_exception(self):
            with self.assertRaises(ValueError):
                self.elitism.k = 0
                self.elitism.k = -15
            
            with self.assertRaises(Exception):
                self.elitism.k = []
                self.elitism.k = object()
