import unittest
import unittest.mock as mock

from search_ai.tests.test_case_with_utils import TestCaseWithUtils


class TestRecombinations(object):
    
    class TestRecombination(TestCaseWithUtils):
        
        def setUp(self):
            self.len_features = 5
            self.number_of_children = 4
            self.number_of_parents = 4
            self.children = [
                self._mock_child()
                for _ in range(self.number_of_children)
            ]
            self.parents = [
                self._mock_parent()
                for _ in range(self.number_of_parents)
            ]
            self.fitness = mock.MagicMock()
            self.fitness.new_blank_individual.side_effect = self.children
        
        def check_recombination_attributes(
                self,
                recombination,
                number_of_children
        ):
            self.assertEqual(
                self.number_of_children,
                self.recombination.number_of_children
            )
            self.assertIs(self.fitness, self.recombination.fitness)
        
        def test_recombination_number_of_children(self):
            self.assertEqual(
                self.recombination.number_of_children,
                self.number_of_children
            )
            
            self.recombination.number_of_children = 1
            self.assertEqual(self.recombination.number_of_children, 1)
            
            self.recombination.number_of_children = 10
            self.assertEqual(self.recombination.number_of_children, 10)
        
        def test_recombination_number_of_children_exception(self):
            with self.assertRaises(ValueError):
                self.recombination.number_of_children = -100
                self.recombination.number_of_children = 0
        
        def test_recombination_fitness(self):
            new_mock = mock.MagicMock()
            self.recombination.fitness = new_mock
            self.assertIs(new_mock, self.recombination.fitness)
        
        def _mock_parent(self):
            parent = mock.MagicMock()
            parent.get_feature_at.return_value = True
            return parent
        
        def _mock_child(self):
            child = mock.MagicMock()
            child.set_feature_at.return_value = None
            child.len_features.return_value = self.len_features
            return child
