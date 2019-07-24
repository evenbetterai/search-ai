import unittest

from search_ai.ga.selection.selection import Selection


class TestSelections(object):
    class TestSelection(unittest.TestCase):
        def setUp(self):
            self.min_number_of_parents = 2
            self.number_of_parents = 3

        def check_selection_attributes(self):
            self.assertEqual(self.selection.number_of_parents, self.number_of_parents)
            self.assertEqual(Selection.MIN_NUMBER_OF_PARENTS, self.min_number_of_parents)

        def test_selection_number_of_parents(self):
            self.assertEqual(self.selection.number_of_parents, self.number_of_parents)

            self.selection.number_of_parents = 2
            self.assertEqual(self.selection.number_of_parents, 2)

            self.selection.number_of_parents = 30
            self.assertEqual(self.selection.number_of_parents, 30)

        def test_selection_number_of_parents_exception(self):
            with self.assertRaises(ValueError):
                self.selection.number_of_parents = 1
                self.selection.number_of_parents = -10
