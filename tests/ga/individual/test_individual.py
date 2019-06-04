import unittest


class TestIndividual(unittest.TestCase):
    def test_binary_individual_fitness(self):
        self.assertEqual(self.ind.fitness, 0)
        self.ind.fitness = 0.6
        self.assertEqual(self.ind.fitness, 0.6)

        with self.assertRaises(ValueError):
            self.ind.fitness = 100

        with self.assertRaises(ValueError):
            self.ind.fitness = -0.1

    def test_individual_age(self):
        self.assertEqual(self.ind.age, 0)
        self.ind.age = 2
        self.assertEqual(self.ind.age, 2)

        with self.assertRaises(ValueError):
            self.ind.age = -1
