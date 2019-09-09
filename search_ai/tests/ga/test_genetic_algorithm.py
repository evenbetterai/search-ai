import types
import unittest.mock as mock

from search_ai.ga.genetic_algorithm import GeneticAlgorithm

from search_ai.tests.test_case_with_utils import TestCaseWithUtils

class TestGeneticAlgorithm(TestCaseWithUtils):

    def setUp(self):
        super(TestGeneticAlgorithm, self).setUp()

        self.u = 10
        self.k = 2
        self.h = self.u * 4
        self.p = 3

        self.rec_times = 4
        self.population = [mock.MagicMock() for _ in range(self.u)]
        self.children = [mock.MagicMock() for _ in range(self.h // self.rec_times)]

        self.fitness = mock.MagicMock()
        self.fitness.run.return_value = None

        self.init = mock.MagicMock()
        self.init.run.return_value = self.population

        self.sel = mock.MagicMock()
        self.sel.run.return_value = self.population[0:self.p]

        self.rec = mock.MagicMock()
        self.rec.run.return_value = self.children
        self.rec_num_of_children = mock.PropertyMock(return_value=self.h // self.rec_times)
        type(self.rec).number_of_children = self.rec_num_of_children

        self.mut = mock.MagicMock()
        self.mut.run.return_value = None
        
        self.replace_dups = mock.MagicMock()
        self.replace_dups.run.return_value = None

        self.elitism = mock.MagicMock()
        self.elitism.run.return_value = None

        self.stop_criteria = lambda ga: ga.current_generation >= 2

        self.ga = GeneticAlgorithm(self.u, self.k, self.h, self.p, self.fitness, self.init, self.sel, self.rec, self.mut, self.replace_dups, self.elitism, self.stop_criteria)

    def test_genetic_algorithm_constructor(self):
        self.check_genetic_algorithm_attributes(self.ga, self.u, self.k, self.h, self.p, self.fitness, self.init, self.sel, self.rec, self.mut, self.replace_dups, self.elitism)
        GeneticAlgorithm(2, 1, 2, 1, None, None, None, self.rec, None, None, None, None)

    def test_genetic_algorithm_constructor_exception(self):
        with self.assertRaises(Exception):
            GeneticAlgorithm(2, 1, 2, 1, None, None, None, None, None, None, None, None)
            GeneticAlgorithm(2, 1, 2, 1, self.fitness, self.init, self.sel, None, self.mut, self.replace_dups, self.elitism, self.stop_criteria)

    def test_genetic_algorithm_u(self):
        self.assertEqual(self.ga.u, self.u)
        
        self.ga.u = 2
        self.assertEqual(self.ga.u, 2)

        self.ga.u = 100
        self.assertEqual(self.ga.u, 100)

    def test_genetic_algorithm_u_expection(self):
        with self.assertRaises(ValueError):
            self.ga.u = 1
            self.ga.u = -5

    def test_genetic_algorithm_k(self):
        self.assertEqual(self.ga.k, self.k)
        
        self.ga.k = 1
        self.assertEqual(self.ga.k, 1)

        self.ga.k = 24
        self.assertEqual(self.ga.k, 24)

    def test_genetic_algorithm_k_expection(self):
        with self.assertRaises(ValueError):
            self.ga.k = 0
            self.ga.k = -10

    def test_genetic_algorithm_h(self):
        self.assertEqual(self.ga.h, self.h)
        
        self.ga.h = self.u
        self.assertEqual(self.ga.h, self.u)

        self.ga.h = 100 * self.u
        self.assertEqual(self.ga.h, 100 * self.u)

    def test_genetic_algorithm_h_expection(self):
        with self.assertRaises(ValueError):
            self.ga.h = self.u - 1
            self.ga.h = self.u - 2 * self.u

        self.ga.u = 2
        with self.assertRaises(ValueError):
            self.ga.h = 1
            self.ga.h = -2

    def test_genetic_algorithm_p(self):
        self.assertEqual(self.ga.p, self.p)
        
        self.ga.p = 2
        self.assertEqual(self.ga.p, 2)

        self.ga.p = 110
        self.assertEqual(self.ga.p, 110)

    def test_genetic_algorithm_p_expection(self):
        with self.assertRaises(ValueError):
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
        self._check_run_method()

    def test_genetic_algorithm_update_population(self):
        with mock.patch('search_ai.ga.genetic_algorithm.sorted') as sorted_mock:
            sorted_mock.return_value = self.children
            ind_age_prop_mock = mock.PropertyMock(side_effect=([0, 0, 1] * len(self.population)))

            for ind in self.population:
                type(ind).age = ind_age_prop_mock

            self.ga.k = 1
            population = list(self.population)
            children = list(self.children)
            self.ga._population = population
            self.ga._children = children
            self.ga.update_population()

            self.assertEqual(self.ga.population, children)
            self.assertEqual(self.ga._current_generation, 1)
            self.replace_dups.run.assert_called_once_with(population, children)
            sorted_mock.assert_called_once_with(children, reverse=True)
            self.elitism.run.assert_called_once_with(population)
            self.assertEqual(ind_age_prop_mock.call_count, 3 * len(self.population))
            self.assertEqual(ind_age_prop_mock.call_args_list, [mock.call(), mock.call(1), mock.call()] * len(self.population))
        

    def check_genetic_algorithm_attributes(self, ga, u, k, h, p, fitness, init, sel, rec, mut, replace_dups, elitism):
        self.assertEqual(ga.u, u)
        self.assertEqual(ga.k, k)
        self.assertEqual(ga.h, h)
        self.assertEqual(ga.p, p)
        self.assertIs(ga.fitness, fitness)
        self.assertIs(ga.initialization, init)
        self.assertIs(ga.selection, sel)
        self.assertIs(ga.recombination, rec)
        self.assertIs(ga.mutation, mut)
        self.assertIs(ga.replace_duplicates, replace_dups)
        self.assertIs(ga.elitism, elitism)
        self.assertIsInstance(ga._stop_criteria, types.FunctionType)
        self.assertEqual(ga.current_generation, 0)
        self.assertIs(ga.population, None)
        self.assertEqual(ga._recombination_times, self.rec_times)

    def _check_run_method(self):
        with mock.patch('search_ai.ga.genetic_algorithm.print') as print_mock:
            self._check_run_method_assertions(print_mock)
            
    def _check_run_method_assertions(self, print_mock):
        def mock_update_population(ga):
                    ga._current_generation += 1
                    
        self.ga.update_population = types.MethodType(mock_update_population, self.ga)
        self.ga.run()

        self.init.run.assert_called_once_with()
        self.assertEqual(self.sel.run.call_count, self.rec_times * 2)
        self.assertEqual(self.rec.run.call_count, self.rec_times * 2)
        self.assertEqual(self.sel.run.call_args_list, [mock.call(self.population) for _ in range(self.rec_times)] * 2)
        self.assertEqual(self.rec.run.call_args_list, [mock.call(self.population[0:self.p]) for _ in range(self.rec_times)] * 2)
        self.assertEqual(self.fitness.run.call_count, self.h * 2)
        self.assertEqual(self.mut.run.call_count, self.h * 2)
        self.assertEqual(self.fitness.run.call_args_list, [mock.call(child) for child in self.children] * 8)
        self.assertEqual(self.mut.run.call_args_list, [mock.call(child) for child in self.children] * 8)
        self.assertEqual(self.ga._current_generation, 2)
        self.assertEqual(print_mock.call_args_list, [mock.call(self.population[0])] * 2)

        self._reset_mocks()
        self.ga._stop_criteria = lambda ga: True
        self.ga.run()

        self.init.run.assert_called_once_with()
        self.assertEqual(self.sel.run.call_count, 0)
        self.assertEqual(self.rec.run.call_count,0)
        self.assertEqual(self.fitness.run.call_count, 0)
        self.assertEqual(self.mut.run.call_count, 0)
        self.assertEqual(self.ga._current_generation, 2)

    def _reset_mocks(self):
        self.fitness.reset_mock()
        self.init.reset_mock()
        self.sel.reset_mock()
        self.rec.reset_mock()
        self.mut.reset_mock()
        self.elitism.reset_mock()
        self.replace_dups.reset_mock()
