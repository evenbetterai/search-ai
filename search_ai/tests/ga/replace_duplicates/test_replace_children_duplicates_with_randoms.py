import unittest.mock as mock

from search_ai.ga.replace_duplicates.replace_children_duplicates_with_randoms import ReplaceChildrenDuplicatesWithRandoms
from search_ai.tests.ga.replace_duplicates.test_replace_children_duplicates import TestReplaceChildrenDuplicatesWrapper


class TestReplaceChildrenDuplicatesWithRandoms(TestReplaceChildrenDuplicatesWrapper.TestReplaceChildrenDuplicates):
    
    def setUp(self):
        super(TestReplaceChildrenDuplicatesWithRandoms, self).setUp()
        
        self.fitness.new_random_individual.side_effect = self.new_children
        self.fitness.run.return_value = None

        self.replace_duplicates = ReplaceChildrenDuplicatesWithRandoms(self.fitness)

    def test_replace_children_duplicates_with_randoms_replace_child(self):
        self.replace_duplicates.replace_child(self.population, self.children, 0)

        self.fitness.new_random_individual.assert_called_once_with()    
        self.fitness.run.assert_called_once_with(self.new_children[0])
