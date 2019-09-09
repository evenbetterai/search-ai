import unittest.mock as mock
from search_ai.ga.replace_duplicates.replacer.random_replacer import RandomReplacer

from search_ai.tests.ga.replace_duplicates.replacer.test_replacer import TestReplacers


class TestRandomReplacer(TestReplacers.TestReplacer):
    
    def setUp(self):
        super(TestRandomReplacer, self).setUp()
        self.child = mock.MagicMock()
        self.fitness.new_random_individual.return_value = self.child
        self.fitness.run.return_value = self.child
        
        self.replace_duplicates = mock.MagicMock()
        self.replacer = RandomReplacer(self.fitness)
    
    def test_random_replacer_constructor(self):
        self.check_replacer_attributes(self.replacer, self.fitness)
    
    def test_replace_in_children(self):
        self.replacer.replace_in_children(self.replace_duplicates, 0)
        self.check_replace_methods(0, self.replace_duplicates._children)
        
        self.reset_mocks()
        self.replacer.replace_in_children(self.replace_duplicates, 5)
        self.check_replace_methods(5, self.replace_duplicates._children)
    
    def test_replace_in_population(self):
        self.replacer.replace_in_population(self.replace_duplicates, 0)
        self.check_replace_methods(
            0,
            self.replace_duplicates._population
        )
        
        self.reset_mocks()
        self.replacer.replace_in_population(self.replace_duplicates, 1)
        self.check_replace_methods(
            1,
            self.replace_duplicates._population
        )
    
    def check_replace_methods(self, index, ind_container):
        self.fitness.new_random_individual.assert_called_once_with()
        self.fitness.run.assert_called_once_with(self.child)
        ind_container.__setitem__.assert_called_once_with(
            index,
            self.child
        )
    
    def reset_mocks(self):
        self.fitness.reset_mock()
        self.replace_duplicates.reset_mock()
        self.child.reset_mock()
