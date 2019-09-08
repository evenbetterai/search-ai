import unittest.mock as mock
import types

from search_ai.ga.genetic_algorithm import GeneticAlgorithm

from search_ai.tests.test_case_with_utils import TestCaseWithUtils

with mock.patch('search_ai.ga.genetic_algorithm.GeneticAlgorithm._recombination.num_of_children', new_callable=mock.PropertyMock) as mock_rec_num_of_children:
    class TestGeneticAlgorithm(TestCaseWithUtils):

        def setUp(self):
            super(TestGeneticAlgorithm, self).setUp()

            self.u = 10
            self.k = 2
            self.h = self.u * 4
            self.p = 3

            self.population = [mock.MagicMock for _ in range(self.u)]
            self.fitness = mock.MagicMock()
            self.init = mock.MagicMock()
            self.init.run.return_value = self.population
            self.sel = mock.MagicMock()
            self.rec = mock.MagicMock()
            self.mut = mock.MagicMock()
            self.replace_dups = mock.MagicMock()
            self.elitism = mock.MagicMock()
            self.stop_criteria = lambda ga: ga.current_generation >= 2

            self.rec_times = 4

            self.ga = GeneticAlgorithm(self.u, self.k, self.h, self.p, self.fitness, self.init, self.sel, self.rec, self.mut, self.replace_dups, self.elitism, self.stop_criteria)

        def test_genetic_algorithm_constructor(self):
            self.check_genetic_algorithm_attributes(self.ga, self.u, self.k, self.h, self.p, self.fitness, self.init, self.sel, self.rec, self.mut, self.replace_dups, self.elitism)

            ga = GeneticAlgorithm(2, 1, 2, 1, None, None, None, None, None, None, None, None)

        def test_genetic_algorithm_u(self):
            self.assertEqual(self.ga.u, self.u)
            
            self.u = 2
            self.assertEqual(self.ga.u, 2)

            self.u = 100
            self.assertEqual(self.ga.u, 100)

        def test_genetic_algorithm_u_expection(self):
            with self.assertException(ValueError):
                self.ga.u = 1
                self.ga.u = -5

        def test_genetic_algorithm_k(self):
            self.assertEqual(self.ga.k, self.k)
            
            self.u = 1
            self.assertEqual(self.ga.u, 1)

            self.u = 24
            self.assertEqual(self.ga.u, 24)

        def test_genetic_algorithm_k_expection(self):
            with self.assertException(ValueError):
                self.ga.u = 0
                self.ga.u = -10

        def test_genetic_algorithm_h(self):
            self.assertEqual(self.ga.h, self.h)
            
            self.h = self.u
            self.assertEqual(self.ga.u, self.u)

            self.h = 100 * self.u
            self.assertEqual(self.ga.h, 100 * self.u)

        def test_genetic_algorithm_h_expection(self):
            with self.assertException(ValueError):
                self.ga.h = self.u - 1
                self.ga.test_genetic_algorithm_h = self.u - 2 * self.u

            self.ga.u = 2
            with self.assertException(ValueError):
                self.ga.h = 1
                self.ga.h = -2

        def test_genetic_algorithm_p(self):
            self.assertEqual(self.ga.p, self.p)
            
            self.p = 2
            self.assertEqual(self.ga.p, 2)

            self.p = 100
            self.assertEqual(self.ga.p, 110)

        def test_genetic_algorithm_p_expection(self):
            with self.assertException(ValueError):
                self.ga.p = 1
                self.ga.p = -3

        def test_genetic_algorithm_fitness(self):
            self.check_simple_property(self.ga, 'fitness', self.fitness)

        def test_genetic_algorithm_initialization(self):
            self.check_simple_property(self.ga, 'initialization', self.init)

        def test_genetic_algorithm_selection(self):
            self.check_simple_property(self.ga, 'selection', self.sel)

        def test_genetic_algorithm_recombination(self):
            self.check_simple_property(self.ga, 'recombination', self.rec)

        def test_genetic_algorithm_mutation(self):
            self.check_simple_property(self.ga, 'mutation', self.mut)

        def test_genetic_algorithm_replace_duplicates(self):
            self.check_simple_property(self.ga, 'replace_duplicates', self.replace_dups)

        def test_genetic_algorithm_elitism(self):
            self.check_simple_property(self.ga, 'elitism', self.elitism)

        def test_genetic_algorithm_run(self):

        def check_genetic_algorithm_attributes(self, ga, u, k, h, p, fitness, init, sel, rec, mut, replace_dups, elitism):
            self.assertEqual(ga.u, u)
            self.assertEqual(ga.k, k)
            self.assertEqual(ga.h, h)
            self.assertEqual(ga.p, p)
            self.assertIs(ga.fitness, fitness)
            self.assertIs(ga.init, init)
            self.assertIs(ga.sel, sel)
            self.assertIs(ga.rec, rec)
            self.assertIs(ga.mut, mut)
            self.assertIs(ga.replace_dups, replace_dups)
            self.assertIs(ga.elitism, elitism)
            self.assertIsInstance(ga._stop_criteria, types.FunctionType)
            self.assertEqual(ga.current_generation, 0)
            self.assertIs(ga.population, None)
