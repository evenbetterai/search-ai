from collections import Sequence
import unittest


class TestCaseWithUtils(unittest.TestCase):

    def cmp_arrays(self, array1, array2):
        self.assertEqual(len(array1), len(array2))

        for i in range(len(array1)):
            self.cmp_array_els(array1[i], array2[i])

    def cmp_array_els(self, el1, el2):
        self.assertEqual(el1, el2)
