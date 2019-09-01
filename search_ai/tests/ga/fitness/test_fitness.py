from search_ai.tests.test_case_with_utils import TestCaseWithUtils


class TestFitnesses(object):

    class TestFitness(TestCaseWithUtils):

        def setUp(self):
            self.len_features = 10

        def check_fitness_constructor(self, fitness, len_features):
            self.assertEqual(fitness.len_features, len_features)

        def test_fitness_len_features(self):
            self.assertEqual(self.fitness.len_features, self.len_features)
            
            self.fitness.len_features = 1
            self.assertEqual(self.fitness.len_features, 1)

            self.fitness.len_features = 100
            self.assertEqual(self.fitness.len_features, 100)

        def test_fitness_len_features_exception(self):
            with self.assertRaises(ValueError):
                self.fitness.len_features = 0
                self.fitness.len_features = -3
