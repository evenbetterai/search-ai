import unittest
from unittest.mock import MagicMock, Mock

from search_ai.ga.fitness.fitness import Fitness
from search_ai.ga.individual.binary_individual import BinaryIndividual
from search_ai.ga.initialization.initialization import Initialization
from search_ai.ga.initialization.initialization_component import InitializationComponent
from search_ai.utils.test_case_with_utils import TestCaseWithUtils


class TestInitialization(TestCaseWithUtils):

    def create_fitness_mock(self, population):
        self.fitness = MagicMock()
        self.fitness.new_random_individual.side_effect = list(
            population
        )
        self.fitness.run.return_value = None

    def create_init_components_mock(
            self, u, init_population_size, population
    ):
        self.n_init_components = 1
        self.init_component = MagicMock()
        self.init_component.run.return_value = list(
            [population[0]] * (init_population_size//2) +
            population[0:init_population_size // 2]
        )
        self.best_individuals_with_init_component = list(
            population[init_population_size//2 -
                       u:init_population_size // 2]
        )[::-1]

    def create_n_individuals(
            self, n, individual_class=BinaryIndividual
    ):
        individuals = [individual_class(n) for _ in range(n)]

        for i in range(n):
            individuals[i].set_feature_at(i, 1)
            individuals[i].fitness = i / n

        return individuals

    def check_initialization_after_creattion(
            self, init, u, init_population_size, n_init_components
    ):
        self.assertEqual(init.u, u)
        self.assertEqual(
            init.init_population_size, init_population_size
        )

        self.check_fitness_interface(init.fitness)

        self.assertEqual(
            len(init.initialization_components), n_init_components
        )

        self.check_initialization_components_interface(
            init.initialization_components
        )

    def check_fitness_interface(self, fitness):
        self.assertTrue(hasattr(fitness, "new_random_individual"))
        self.assertTrue(hasattr(fitness, "run"))

    def check_initialization_components_interface(
            self, init_components
    ):
        for init_component in init_components:
            self.assertTrue(hasattr(init_component, "run"))

    def check_fitness_behaviour(self, fitness, individuals):
        self.assertEqual(
            fitness.new_random_individual.call_count, len(individuals)
        )
        self.assertEqual(fitness.run.call_count, len(individuals))

        for individual in individuals:
            fitness.run.assert_any_call(individual)

    def check_initialization_components_behaviour(
            self, init_components
    ):
        for init_component in init_components:
            self.assertEqual(init_component.run.call_count, 1)
            init_component.run.assert_called_with(self.population)

    def setUp(self):
        self.u = 10
        self.init_population_size = 50
        self.population = self.create_n_individuals(
            self.init_population_size
        )
        self.best_individuals = list(
            self.population[self.init_population_size - self.u:]
        )[::-1]

        self.create_fitness_mock(self.population)
        self.create_init_components_mock(
            self.u, self.init_population_size, self.population
        )

        self.init = Initialization(
            self.u, self.fitness, self.init_population_size,
            (self.init_component, )
        )

    def test_initialization_constructor(self):
        self.check_initialization_after_creattion(
            self.init, self.u, self.init_population_size,
            self.n_init_components
        )

        u = 2
        other_init = Initialization(u, self.fitness, u)
        self.check_initialization_after_creattion(other_init, u, u, 0)

    def test_initialization_constructor_exception(self):
        with self.assertRaises(ValueError):
            Initialization(-1, None, 10)
            Initialization(1, None, 9)
            Initialization(10, None, -4)
            Initialization(10, None, 9)

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
        self.check_fitness_interface(self.init.fitness)

    def test_initialization_init_components(self):
        self.check_initialization_components_interface(
            self.init.initialization_components
        )

    def test_initialization_run(self):
        population = self.init.run()
        self.cmp_arrays(
            population, self.best_individuals_with_init_component
        )
        self.check_fitness_behaviour(self.init.fitness, self.population)
        self.check_initialization_components_behaviour(
            self.init.initialization_components
        )

        self.init.initialization_components = ()
        self.create_fitness_mock(self.population)
        self.init.fitness = self.fitness
        population = self.init.run()
        self.cmp_arrays(population, self.best_individuals)
        self.check_fitness_behaviour(self.init.fitness, self.population)
        self.assertEqual(self.init_component.call_count, 0)

    def test_initialization_run_exception(self):
        self.init.fitness = object()

        with self.assertRaises(Exception):
            self.init.run()

        self.init.fitness = self.fitness
        self.init.initialization_components = (object(), )

        with self.assertRaises(Exception):
            self.init.run()
