import unittest.mock as mock

from search_ai.tests.ga.replace_duplicates.test_replace_duplicates import TestReplaceDuplicatesWrapper

class TestReplaceChildrenDuplicatesWrapper(object):

    class TestReplaceChildrenDuplicates(TestReplaceDuplicatesWrapper.TestReplaceDuplicates):

        def setUp(self):
            super(TestReplaceChildrenDuplicatesWrapper.TestReplaceChildrenDuplicates, self).setUp()
            self.u = 10
            self.l = self.u * 3
            self.diff = 2
            self.population = [mock.MagicMock() for _ in range(self.u)]
            self.children = [mock.MagicMock() for _ in range(self.l)]
            self.old_children = list(self.children)
            self.new_children = [mock.MagicMock() for _ in range(self.diff)]

            self.replace_duplicates = None

        def test_replace_duplicates_with_randoms(self):
            with mock.patch('search_ai.ga.replace_duplicates.replace_children_duplicates.Search') as mock_search:
                mock_search.sequencial_search.side_effect=[-1 for _ in range(self.l - self.diff)] + [i for i in range(self.diff)]
                self.replace_duplicates.run(population=self.population, children=self.children)
                self.assertEqual(mock_search.sequencial_search.call_count, len(self.old_children))

                for child in self.old_children:
                    mock_search.sequencial_search.assert_any_call(self.population, child, mock.ANY)
