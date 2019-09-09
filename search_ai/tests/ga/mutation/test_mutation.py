from search_ai.tests.test_case_with_utils import TestCaseWithUtils


class TestMutations(object):
    
    class TestMutation(TestCaseWithUtils):
        
        def test_mutation_constructor(self):
            self.assertEqual(
                self.mutation.mutation_prob,
                self.mutation_prob
            )
        
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
