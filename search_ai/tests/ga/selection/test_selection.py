from search_ai.ga.individual.binary_individual import BinaryIndividual
from search_ai.ga.selection.selection import Selection

from search_ai.tests.test_case_with_utils import TestCaseWithUtils


class TestSelections(object):
    class TestSelection(TestCaseWithUtils):
        def setUp(self):
            self.min_number_of_parents = 2
            self.number_of_parents = 3

            self.one_individual = [BinaryIndividual(5) for _ in range(1)]
            self.one_individual[0].fitness = 1

            self.two_individuals = [BinaryIndividual(5) for _ in range(2)]
            self.two_individuals[0].fitness = 1
            self.two_individuals[1].fitness = 1

            self.five_individuals = [BinaryIndividual(5) for _ in range(5)]
            self.five_individuals[0].fitness = 1
            self.five_individuals[1].fitness = 0.1
            self.five_individuals[2].fitness = 0.1
            self.five_individuals[3].fitness = 0.1
            self.five_individuals[4].fitness = 0.1

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
