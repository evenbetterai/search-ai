import unittest
from unittest.mock import MagicMock, Mock


from search_ai.ga.fitness.fitness import Fitness
from search_ai.ga.individual.binary_individual import BinaryIndividual
from search_ai.ga.initialization.initialization import Initialization
from search_ai.ga.initialization.initialization_component import InitializationComponent

class TestInitialization(unittest.TestCase):

    def create_n_individuals(self, n, individual_class=BinaryIndividual):
        individuals = [individual_class(n) for i in range(len(n))]

        for i in range(len(n)):
            individuals[i].set_feature_at(i, 1)

    def check_initialization_after_creattion(self, init, u, init_population_size, n_init_components):
        self.assertEqual(init.u, u)
        self.assertEqual(init.init_population_size, init_population_size)

        self.check_fitness_interface(init.fitness)

        self.assertEqual(len(init.initialization_components), n_init_components)

        for init_component in init.initialization_components:
            self.check_initialization_component_interface(init_component)

    def check_fitness_interface(self, fitness):
        self.assertTrue(hasattr(self.initialization.fitness, "new_random_individual"))
        self.assertTrue(hasattr(self.initialization.fitness, "run"))

    def check_initi_component_interface(self, init_component):
        self.assertTrue(hasattr(init_component, "run"))

    def setUp(self):
        self.u = 10
        self.init_population_size = 50
        self.all_individuals = self.create_n_individuals(self.init_population_size)

        self.fitness = MagicMock()
        self.fitness.new_random_individual.side_effect = self.all_individuals
        self.fitness.run.side_effect = [i / len(self.all_individuals) for i in range(len(self.all_individuals))]

        self.n_init_components = 1
        self.init_component = MagicMock()
        self.init_component.run.return_value = self.all_individuals[0:self.init_population_size // 2] * 2 

        self.init = Initialization(self.u, self.fitness, self.init_population_size)

    def test_initialization_constructor(self):
        self.check_initialization_after_creattion(self.init, self.u, self.init_population_size, self.n_init_components)

        u = 3
        other_init = Initialization(u, self.fitness)
        self.check_initialization_after_creattion(other_init, u, u, 0)

    def test_initialization_constructor_exception(self):
        with self.assertRaises(ValueError):
            Initialization(-1, None)
            Initialization(1, None)
            Initialization(10, None, -4)
            Initialization(10, None, 9)

    def test_initialization_u(self):
        self.assertEqual(self.init.u, self.u)

        self.init.u = self.init_population_size
        self.assertEqual(self.init.u, self.init_pop_size)

        self.init1.u = 2
        self.assertEqual(self.init.u, 2)

    def test_initialization_u_exception(self):
        with self.assertRaises(ValueError):
            self.init.u = 1
            self.init.u = -2
            self.init.u = self.init.init_population_size + 1

    def test_initialization_init_population_size(self):
        self.assertEqual(self.init.init_population_size, self.init_population_size)
        
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

    def test_initialization_run(self):
