import unittest

from search_ai.utils.search import Search


class TestSearch(unittest.TestCase):

    def setUp(self):
        self.list_to_test_key = [(1, 'd'), (1, 'c'), (1, 'b'), (1, 'a')]
        self.key_first = lambda el: el[0]
        self.key_second = lambda el: el[1]
        self.key_binary = lambda el: ord('z') - ord(el[1])

    def test_search_sequencial_search(self):
        self.assertEqual(Search.sequencial_search([], 1), -1)
        self.assertEqual(Search.sequencial_search([2], 1), -1)
        self.assertEqual(Search.sequencial_search([1], 1), 0) 

        self.assertEqual(Search.sequencial_search([1, 2], 1), 0)
        self.assertEqual(Search.sequencial_search([1, 2], 2), 1)

        self.assertEqual(Search.sequencial_search([1, 2, 3, 4, 5], 1), 0)
        self.assertEqual(Search.sequencial_search([1, 2, 3, 4, 5], 2), 1)
        self.assertEqual(Search.sequencial_search([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(Search.sequencial_search([1, 2, 3, 4, 5], 4), 3)
        self.assertEqual(Search.sequencial_search([1, 2, 3, 4, 5], 5), 4)

    def test_search_sequencial_search_with_key(self):
        self.assertEqual(Search.sequencial_search(self.list_to_test_key, (1, 'e'), self.key_first), 0)
        self.assertEqual(Search.sequencial_search(self.list_to_test_key, (1, 'e'), self.key_second), -1)

        self.assertEqual(Search.sequencial_search(self.list_to_test_key, (2, 'a'), self.key_second), 3)
        self.assertEqual(Search.sequencial_search(self.list_to_test_key, (2, 'a'), self.key_first), -1)

        self.assertEqual(Search.sequencial_search(self.list_to_test_key, (2, 'd'), self.key_second), 0)
        self.assertEqual(Search.sequencial_search(self.list_to_test_key, (2, 'd'), self.key_first), -1)

        self.assertEqual(Search.sequencial_search(self.list_to_test_key, (2, 'c'), self.key_second), 1)
        self.assertEqual(Search.sequencial_search(self.list_to_test_key, (2, 'c'), self.key_first), -1)

    def test_search_binary_search(self):
        self.assertEqual(Search.binary_search([], 1), -1)
        self.assertEqual(Search.binary_search([2], 1), -1)
        self.assertEqual(Search.binary_search([1], 1), 0) 

        self.assertEqual(Search.binary_search([1, 2], 1), 0)
        self.assertEqual(Search.binary_search([1, 2], 2), 1)

        self.assertEqual(Search.binary_search([1, 2, 3, 4, 5], 1), 0)
        self.assertEqual(Search.binary_search([1, 2, 3, 4, 5], 2), 1)
        self.assertEqual(Search.binary_search([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(Search.binary_search([1, 2, 3, 4, 5], 4), 3)
        self.assertEqual(Search.binary_search([1, 2, 3, 4, 5], 5), 4)

    def test_search_binary_search_with_key(self):
        self.assertEqual(Search.binary_search(self.list_to_test_key, (1, 'e'), self.key_first), 1)
        self.assertEqual(Search.binary_search(self.list_to_test_key, (1, 'e'), self.key_second), -1)

        self.assertEqual(Search.binary_search(self.list_to_test_key, (2, 'd'), self.key_binary), 0)
        self.assertEqual(Search.binary_search(self.list_to_test_key, (2, 'd'), self.key_first), -1)

        self.assertEqual(Search.binary_search(self.list_to_test_key, (2, 'a'), self.key_binary), 3)
        self.assertEqual(Search.binary_search(self.list_to_test_key, (2, 'a'), self.key_first), -1)

        self.assertEqual(Search.binary_search(self.list_to_test_key, (2, 'b'), self.key_binary), 2)
        self.assertEqual(Search.binary_search(self.list_to_test_key, (2, 'b'), self.key_first), -1)
