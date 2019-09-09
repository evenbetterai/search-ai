import unittest.mock as mock

from search_ai.ga.elitism.percentage_elitism import PercentageElitism

from search_ai.tests.ga.elitism.test_elitism import TestElitisms


class TestPercentageElitism(TestElitisms.TestElitism):
    
    def setUp(self):
        super(TestPercentageElitism, self).setUp()
        
        self.u = 10
        self.l = self.u * 2
        self.percentage_elitism = 0.2
        self.diff = int(self.u * self.percentage_elitism)
        
        self.population_mocks = [
            self._create_ind_mock(self.k - 1) for _ in range(self.diff)
        ]
        self.population_mocks += [
            self._create_ind_mock(self.k - 2)
            for _ in range(self.u - self.diff)
        ]
        self.population_objs = [
            ind['obj'] for ind in self.population_mocks
        ]
        self.children_mocks = [
            self._create_ind_mock(0) for _ in range(self.l)
        ]
        self.children_objs = [ind['obj'] for ind in self.children_mocks]
        
        self.elitism = PercentageElitism(
            self.k,
            self.percentage_elitism
        )
    
    def test_percentage_elitism_constructor(self):
        self.check_elitism_constructor(self.elitism, self.k)
        self.assertEqual(self.elitism.elitism, self.percentage_elitism)
    
    def test_percentage_elitism_elitism(self):
        self.assertEqual(self.elitism.elitism, self.percentage_elitism)
        
        self.elitism.elitism = 0
        self.assertEqual(self.elitism.elitism, 0)
        
        self.elitism.elitism = 1
        self.assertEqual(self.elitism.elitism, 1)
    
    def test_percentage_elitism_elitism_exception(self):
        with self.assertRaises(ValueError):
            self.elitism.elitism = -0.00001
            self.elitism.elitism = 1.2
            self.elitism.elitism = -100
        
        with self.assertRaises(Exception):
            self.elitism.elitism = []
            self.elitism.elitism = object()
    
    def test_percentage_elitism_run_no_calls(self):
        with mock.patch('search_ai.ga.elitism.percentage_elitism.max'
                        ) as mock_max:
            mock_max.side_effect = self.children_objs[0:self.diff]
            self.elitism.run(self.population_objs, self.children_objs)
            
            for ind_mock in self.population_mocks + self.children_mocks[
                    self.diff:]:
                ind_mock['age_prop_mock'].assert_not_called()
            
            for ind_mock in self.children_mocks[0:self.diff]:
                ind_mock['age_prop_mock'].assert_called_once_with()
    
    def test_percentage_elitism_run_one_call(self):
        with mock.patch('search_ai.ga.elitism.percentage_elitism.max'
                        ) as mock_max:
            mock_max.side_effect = self.population_objs[
                len(self.population_objs) - self.diff:]
            self.elitism.run(self.population_objs, self.children_objs)
            
            for ind_mock in self.population_mocks[
                    0:len(self.population_mocks) -
                    self.diff] + self.children_mocks:
                ind_mock['age_prop_mock'].assert_not_called()
            
            for ind_mock in self.population_mocks[len(self.
                                                      population_objs) -
                                                  self.diff:]:
                ind_mock['age_prop_mock'].assert_called_once_with()
    
    def test_percentage_elitism_run_one_call_2(self):
        with mock.patch('search_ai.ga.elitism.percentage_elitism.max'
                        ) as mock_max:
            mock_max.side_effect = self.children_objs[
                0:self.diff - 1] + [self.population_objs[0]]
            self.elitism.run(self.population_objs, self.children_objs)
            
            for ind_mock in self.population_mocks[
                    1:] + self.children_mocks[self.diff - 1:]:
                ind_mock['age_prop_mock'].assert_not_called()
            
            self.assertEqual(
                self.population_mocks[0]
                ['age_prop_mock'].call_args_list,
                [mock.call(),
                 mock.call(self.k - 2)]
            )
            
            for ind_mock in self.children_mocks[0:self.diff - 1]:
                ind_mock['age_prop_mock'].assert_called_once_with()
    
    def test_percentage_elitism_run_diff_calls(self):
        with mock.patch('search_ai.ga.elitism.percentage_elitism.max'
                        ) as mock_max:
            mock_max.side_effect = self.population_objs[0:self.diff]
            self.elitism.run(self.population_objs, self.children_objs)
            
            for ind_mock in self.population_mocks[
                    self.diff:] + self.children_mocks:
                ind_mock['age_prop_mock'].assert_not_called()
            
            for ind_mock in self.population_mocks[0:self.diff]:
                self.assertEqual(
                    ind_mock['age_prop_mock'].call_args_list,
                    [mock.call(),
                     mock.call(self.k - 2)]
                )
    
    def _create_ind_mock(self, age):
        ind = {}
        ind['age_prop_mock'] = mock.PropertyMock(return_value=age)
        ind['obj'] = mock.MagicMock()
        type(ind['obj']).age = ind['age_prop_mock']
        return ind
