from search_ai.utils.test_case_with_utils import TestCaseWithUtils


class TestIndividuals:

    class TestIndividual(TestCaseWithUtils):

        def test_individual_constructor(self):
            self.assertEqual(self.ind.age, 0)
            self.assertEqual(self.ind.fitness, 0)

        def test_individual_fitness(self):
            self.assertEqual(self.ind.fitness, 0)

            self.ind.fitness = 0.6
            self.assertAlmostEqual(self.ind.fitness, 0.6)

            self.ind.fitness += 0.21
            self.assertAlmostEqual(self.ind.fitness, 0.81)

        def test_individual_fitness_exception(self):
            with self.assertRaises(ValueError):
                self.ind.fitness = 100

            with self.assertRaises(ValueError):
                self.ind.fitness = -0.1

        def test_individual_age(self):
            self.assertEqual(self.ind.age, 0)

            self.ind.age = 2
            self.assertEqual(self.ind.age, 2)

            self.ind.age += 1
            self.assertEqual(self.ind.age, 3)

        def test_individual_age_exception(self):
            with self.assertRaises(ValueError):
                self.ind.age = -1

        def check_individual_comparators(
                self, low_individual, middle_individual, high_individual
        ):
            self.assertNotEqual(low_individual, middle_individual)
            self.assertTrue(middle_individual < high_individual)
            self.assertTrue(middle_individual >= low_individual)
            self.assertTrue(high_individual > low_individual)

            low_individual.fitness = middle_individual.fitness
            self.assertEqual(
                low_individual.fitness, middle_individual.fitness
            )
            middle_individual.fitness = high_individual.fitness
            self.assertTrue(middle_individual >= high_individual)
