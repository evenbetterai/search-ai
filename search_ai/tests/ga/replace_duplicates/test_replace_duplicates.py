import unittest
import unittest.mock as mock

from search_ai.tests.test_case_with_utils import TestCaseWithUtils

class TestReplaceDuplicatesWrapper(object):

    class TestReplaceDuplicates(TestCaseWithUtils):

        def setUp(self):
            super(TestReplaceDuplicatesWrapper.TestReplaceDuplicates, self).setUp()
            self.replacer = mock.MagicMock()

        def check_recplace_duplicates_attributes(self, replace_duplicates, replacer):
           self.assertIs(replacer, replace_duplicates.replacer)

        def test_replace_duplicates_replacer(self):
            self.assertIs(self.replacer, self.replace_duplicates.replacer)

            new_replacer = object()
            self.replace_duplicates.replacer = new_replacer
            self.assertIs(self.replace_duplicates.replacer, new_replacer)
