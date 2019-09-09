import unittest.mock as mock

from search_ai.ga.replace_duplicates.replace_population_duplicates import ReplacePopulationDuplicates

from search_ai.tests.ga.replace_duplicates.test_replace_duplicates import TestReplaceDuplicatesWrapper


class TestReplacePopulationDuplicates(
        TestReplaceDuplicatesWrapper.TestReplaceDuplicates):
    
    def setUp(self):
        super(TestReplacePopulationDuplicates, self).setUp()
        self.u = 10
        self.diff = 2
        self.population = [mock.MagicMock() for _ in range(self.u)]
        
        self.replace_duplicates = ReplacePopulationDuplicates(
            self.replacer
        )
    
    def test_replace_duplicates_constructor(self):
        self.check_recplace_duplicates_attributes(
            self.replace_duplicates,
            self.replacer
        )
        self.check_recplace_duplicates_attributes(
            ReplacePopulationDuplicates(None),
            None
        )
    
    def test_replace_duplicates_run(self):
        with mock.patch(
                'search_ai.ga.replace_duplicates.replace_population_duplicates.Search'
        ) as mock_search:
            mock_search.sequencial_search.side_effect = [
                -1 for _ in range(self.u - self.diff)
            ] + [i for i in range(self.diff)]
            self.replace_duplicates.run(population=self.population)
            self.assertEqual(
                self.population,
                self.replace_duplicates._population
            )
            self.assertEqual(
                mock_search.sequencial_search.call_count,
                self.u
            )
            
            for i in range(self.u):
                other_population = list(self.population)
                other_population.pop(i)
                mock_search.sequencial_search.assert_any_call(
                    other_population,
                    self.population[i],
                    mock.ANY
                )
            
            self.assertEqual(
                self.replacer.replace_in_children.call_count,
                0
            )
            self.assertEqual(
                self.replacer.replace_in_population.call_count,
                self.diff
            )
            
            for i in range(self.diff):
                self.replacer.replace_in_population.assert_any_call(
                    self.replace_duplicates,
                    self.u - self.diff + i
                )
