from unittest.mock import MagicMock

from search_ai.tests.ga.test_case_with_population import TestCaseWithPopulation


class TestReplaceDuplicatesWithRandoms(TestCaseWithPopulation):

    def setUp(self):
        self.fitness = MagicMock()
