# import unittest

# from search_ai.ga.initialization.initialization import Initializarion
# from search_ai.ga.fitness.binary_fitness_example import BinaryFitnessExample
# from search_ai.ga.fitness.continuous_fitness_example import ContinuousFitnessExample

# class TestInitialization(unittest.TestCase):
# 	def setUp(self):
# 		self.u = 10
# 		self.init_pop_size = 50
# 		self.init1 = Initialization(BinaryFitnessExample(), 10, 50, (InitLeafExample1, InitLeafExample2))
# 		self.init2 = Initialization(ContinuousFitnessExample(), 10, 50, [])

#     def test_initialization_constructor(self):
#       self.assertEqual(self.init1.u, self.u)
#       self.assertEqual(self.init2.u, self.u)
#       self.assertEqual(self.init1.init_population_size, self.init_pop_size)
#       self.assertEqual(self.init2.init_population_size, self.init_pop_size)
#       self.assertTrue(isinstance(self.init1.initialization_leafs[i], InitLeafExample1))
#       self.assertTrue(isinstance(self.init1.initialization_leaf[1],InitLeafExample2))
#       self.assertTrue(self.init2.initialization_leafs.empty())

#     def test_initialization_u(self):
#       self.assertEqual(self.init1.u, self.u)
#       self.init1.u = self.ini_pop_size - 1
#       self.assertEqual(self.init1.u, self.init_pop_size - 1)
#       self.init1.u = 2
#       self.init1.u = self.init_pop_size

#     def test_initialization_u_exceptions(self):
#       self.assertRaise(ValueError, lambda: self.init1.u = 1)
#       self.assertRaise(ValueError, lambda: self.init1.u = 0)
#       self.assertRaise(ValueError, lambda: self.init1.u = self.init_pop_size + 1)
