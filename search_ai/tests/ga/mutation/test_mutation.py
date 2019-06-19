from search_ai.utils.test_case_with_utils import TestCaseWithUtils


class TestMutations(object):

    class TestMutation(TestCaseWithUtils):

        def test_mutation_constructor(self):
            self.assertEqual(self.mutation.mutation_prob, self.mutation_prob)

        def test_mutation_mutation_prob(self):
            self.mutation.mutation_prob = 1
            self.assertEqual(self.mutation.mutation_prob, 1)

            self.mutation.mutation_prob = 0
            self.assertEqual(self.mutation.mutation_prob, 0)

            self.mutation.mutation_prob = 0.23
            self.assertAlmostEqual(self.mutation.mutation_prob, 0.23)

        def test_mutation_mutation_prob_exception(self):
            with self.assertRaises(ValueError):
                self.mutation.mutation_prob = -0.1
                self.mutation.mutation_prob = 100

        def test_mutation_run(self):
            self.mutation.mutation_prob = 0
            features_before_mutation = list(self.individual.features)
            self.mutation.run(self.individual)
            self.cmp_arrays(self.individual.features, features_before_mutation)

            self.mutation.mutation_prob = 1
            features_before_mutation = [not feature for feature in self.individual.features]
            self.mutation.run(self.individual)
            self.cmp_arrays(self.individual.features, features_before_mutation)

            self.mutation.mutation_prob = 0.3
            self.mutation.run(self.individual)

            for feature in self.individual.features:
                self.assertTrue(feature == 0 or feature == 1)

