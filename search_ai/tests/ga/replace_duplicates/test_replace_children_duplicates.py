import unittest.mock as mock

from search_ai.ga.replace_duplicates.replace_children_duplicates import ReplaceChildrenDuplicates

from search_ai.tests.ga.replace_duplicates.test_replace_duplicates import TestReplaceDuplicatesWrapper


class TestReplaceChildrenDuplicates(
        TestReplaceDuplicatesWrapper.TestReplaceDuplicates):
    
    def setUp(self):
        super(TestReplaceChildrenDuplicates, self).setUp()
        self.u = 10
        self.l = self.u * 3
        self.diff = 2
        self.population = [mock.MagicMock() for _ in range(self.u)]
        self.children = [mock.MagicMock() for _ in range(self.l)]
        self.old_children = list(self.children)
        self.new_children = [mock.MagicMock() for _ in range(self.diff)]
        
        self.replace_duplicates = ReplaceChildrenDuplicates(
            self.replacer
        )
    
    def test_replace_duplicates_constructor(self):
        self.check_recplace_duplicates_attributes(
            self.replace_duplicates,
            self.replacer
        )
        self.check_recplace_duplicates_attributes(
            ReplaceChildrenDuplicates(None),
            None
        )
    
    def test_replace_duplicates_run(self):
        with mock.patch(
                'search_ai.ga.replace_duplicates.replace_children_duplicates.Search'
        ) as mock_search:
            mock_search.sequencial_search.side_effect = [
                -1 for _ in range(self.l - self.diff)
            ] + [i for i in range(self.diff)]
            self.replace_duplicates.run(
                population=self.population,
                children=self.children
            )
            self.assertEqual(
                self.population,
                self.replace_duplicates._population
            )
            self.assertEqual(
                self.children,
                self.replace_duplicates._children
            )
            self.assertEqual(
                mock_search.sequencial_search.call_count,
                len(self.old_children)
            )
            
            for child in self.old_children:
                mock_search.sequencial_search.assert_any_call(
                    self.population,
                    child,
                    mock.ANY
                )
            
            self.assertEqual(
                self.replacer.replace_in_children.call_count,
                self.diff
            )
            self.assertEqual(
                self.replacer.replace_in_population.call_count,
                0
            )
            
            for i in range(self.diff):
                self.replacer.replace_in_children.assert_any_call(
                    self.replace_duplicates,
                    self.l - self.diff + i
                )
