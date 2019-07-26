from collections import Sequence
import unittest


class TestCaseWithUtils(unittest.TestCase):

    def cmp_arrays(self, array1, array2, cmp = lambda el1, el2: el1 == el2):
        self.assertEqual(len(array1), len(array2))

        for i in range(len(array1)):
            self.assertTrue(cmp(array1[i], array2[i]))

    def el_in_array(self, array, el, cmp = lambda el1, el2: el1 == el2):
        count = 0
        for array_el in array:
            if cmp(el, array_el):
                count += 1

        return count
