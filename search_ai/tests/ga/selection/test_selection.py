from search_ai.ga.individual.binary_individual import BinaryIndividual
from search_ai.ga.selection.selection import Selection

from search_ai.tests.ga.test_case_with_population import TestCaseWithPopulation


class TestSelections(object):
    class TestSelection(TestCaseWithPopulation):
        def setUp(self):
            self.min_number_of_parents = 2
            self.number_of_parents = 3

            self.one_individual = self.create_population(1, None, None, [1])
            self.two_individuals = self.create_population(2, None, None, [1, 1])
            self.five_individuals = self.create_population(5, None, None, [1, 0.1, 0.1, 0.1, 0.1])

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

        def el1_is_el2(self, el1, el2):
            return el1 is el2
