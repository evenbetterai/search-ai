import unittest
import unittest.mock as mock

from search_ai.tests.test_case_with_utils import TestCaseWithUtils

class TestReplaceDuplicatesWrapper(object):

    class TestReplaceDuplicates(TestCaseWithUtils):

        def setUp(self):
            self.fitness = mock.MagicMock()

        def check_recplace_duplicates_attributes(self, replace_duplucates, fitness):
           self.assertIs(self.fitness, self.replace_duplicates.fitness)

        def test_replace_duplicates_fitness(self):
            self.assertIs(self.fitness, self.replace_duplicates.fitness)

            new_fitness = object()
            self.replace_duplicates.fitness = new_fitness
            self.assertIs(self.replace_duplicates, new_fitness)
