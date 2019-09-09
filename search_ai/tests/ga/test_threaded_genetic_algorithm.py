import types
import unittest.mock as mock

from search_ai.ga.threaded_genetic_algorithm import ThreadedGeneticAlgorithm

from search_ai.tests.ga.test_genetic_algorithm import TestGeneticAlgorithm


class TestThreadedGeneticAlgorithm(TestGeneticAlgorithm):
    
    def setUp(self):
        super(TestThreadedGeneticAlgorithm, self).setUp()
        self.ga = ThreadedGeneticAlgorithm(
            self.u,
            self.k,
            self.h,
            self.p,
            self.fitness,
            self.init,
            self.sel,
            self.rec,
            self.mut,
            self.replace_dups,
            self.elitism,
            self.stop_criteria
        )
    
    def _check_run_method(self):
        with mock.patch('search_ai.ga.threaded_genetic_algorithm.print'
                        ) as print_mock:
            self._check_run_method_assertions(print_mock)
