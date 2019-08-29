import unittest
from search_ai.utils.bitarray import BitArray

class TestBitArray(unittest.TestCase):
    
    def setUp(self):
        self.str_number = "101001"
        self.int_number = 41
        self.bitarray = BitArray(self.str_number)
        
    def test_bitarray_str(self):
        self.assertEqual(str(self.bitarray), self.str_number)
        self.assertEqual(str(BitArray()), "")
        
    def test_bitarray_int(self):
        self.assertEqual(int(self.bitarray), self.int_number)

    def test_bitarray_int_exception(self):
        with self.assertRaises(Exception):
            int(BitArray())
