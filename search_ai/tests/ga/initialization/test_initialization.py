import unittest.mock as mock

from search_ai.ga.fitness.fitness import Fitness
from search_ai.ga.individual.binary_individual import BinaryIndividual
from search_ai.ga.initialization.initialization import Initialization
from search_ai.tests.ga.test_case_with_population import TestCaseWithPopulation


class TestInitialization(TestCaseWithPopulation):

    def setUp(self):
        self.u = 10
        self.init_population_size = 50
        self.population = [mock.MagicMock() for _ in range(self.init_population_size)]
        self._mock_fitness(self.population)
        self._mock_replace_duplicates()

        self.init = Initialization(
            self.u, self.init_population_size, self.fitness, self.replace_duplicates
        )

    def test_initialization_constructor(self):
        self._check_initialization_after_creattion(
            self.init, self.u, self.init_population_size, self.fitness, self.replace_duplicates
        )

        u = 2
        other_init = Initialization(u, u, None, None)
        self._check_initialization_after_creattion(other_init, u, u, None, None)

    def test_initialization_constructor_exception(self):
        with self.assertRaises(ValueError):
            Initialization(-1, 10, None, None)
            Initialization(1, 9, None, None)
            Initialization(10, -4, None, None)
            Initialization(10, 9, object(), object())

    def test_initialization_u(self):
        self.assertEqual(self.init.u, self.u)

        self.init.u = self.init_population_size
        self.assertEqual(self.init.u, self.init_population_size)

        self.init.u = 2
        self.assertEqual(self.init.u, 2)

    def test_initialization_u_exception(self):
        with self.assertRaises(ValueError):
            self.init.u = 1
            self.init.u = -2
            self.init.u = self.init.init_population_size + 1

    def test_initialization_init_population_size(self):
        self.assertEqual(
            self.init.init_population_size, self.init_population_size
        )

        self.init.init_population_size = self.u
        self.assertEqual(self.init.init_population_size, self.u)

        self.init.init_population_size = self.u * 50
        self.assertEqual(self.init.init_population_size, self.u * 50)

    def test_initialization_init_population_size_exception(self):
        with self.assertRaises(ValueError):
            self.init.init_population_size = self.u - 1
            self.init.init_population_size = 1
            self.init.init_population_size = -19

    def test_initialization_fitness(self):
        self.assertIs(self.init.fitness, self.fitness)

        new_fitness = object()
        self.init.fitness = new_fitness
        self.assertIs(self.init.fitness, new_fitness)

    def test_initialization_replace_duplicates(self):
        self.assertIs(self.init.replace_duplicates, self.replace_duplicates)
        
        new_replace_duplicates = object()
        self.init.replace_duplicates = new_replace_duplicates
        self.assertIs(self.init.replace_duplicates, new_replace_duplicates)

    def test_initialization_run(self):
        with mock.patch('search_ai.ga.initialization.initialization.sorted') as mock_sorted:
            mock_sorted.return_value = self.population
            population = self.init.run()

            mock_sorted.assert_called_once_with(self.population, reverse=True)
            self.cmp_arrays(population, self.population[0:self.u])
            self._check_fitness_behaviour(self.init.fitness, self.population)
            self._check_replace_duplicates_behaviour(self.init.replace_duplicates, self.population)

    def test_initialization_run_exception(self):
        self.init.fitness = object()

        with self.assertRaises(Exception):
            self.init.run()

        self.init.fitness = self.fitness
        self.init.initialization_components = (object(), )

        with self.assertRaises(Exception):
            self.init.run()

    def _mock_fitness(self, population):
        self.fitness = mock.MagicMock()
        self.fitness.new_random_individual.side_effect = list(population)
        self.fitness.run.return_value = None

    def _mock_replace_duplicates(self):
        self.replace_duplicates = mock.MagicMock()
        self.replace_duplicates.run.return_value = None

    def _check_initialization_after_creattion(
            self, init, u, init_population_size, fitness, replace_duplicates
    ):
        self.assertEqual(init.u, u)
        self.assertEqual(
            init.init_population_size, init_population_size
        )

        self.assertIs(init.fitness, fitness)
        self.assertIs(init.replace_duplicates, replace_duplicates)

    def _check_fitness_behaviour(self, fitness, population):
        self.assertEqual(
            fitness.new_random_individual.call_count, len(population)
        )
        self.assertEqual(fitness.run.call_count, len(population))

        for i in range(len(fitness.run.call_args_list)):
            self.assertEqual(fitness.run.call_args_list[i], mock.call(population[i]))
            self.assertEqual(fitness.new_random_individual.call_args_list[i], mock.call())

    def _check_replace_duplicates_behaviour(self, replace_duplicates, population):
        replace_duplicates.run.assert_called_once_with(population)
