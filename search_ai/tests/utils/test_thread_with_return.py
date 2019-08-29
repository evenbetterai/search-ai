import unittest
from search_ai.utils.thread_with_return import ThreadWithReturn


class TestThreadWithReturn(unittest.TestCase):

    def setUp(self):
        self.thread_args = (5,)
        self.thread_should_return = 6
        self.thread = ThreadWithReturn(target=lambda x: x+1, args=self.thread_args)
        
    def test_thread_with_return_init(self):
        self.assertEqual(self.thread._return, None)
        self.assertEqual(ThreadWithReturn()._return, None)
        self.assertEqual(ThreadWithReturn("something", lambda: print(1), "b", (2,), {"c": 3})._return, None)
        
    def test_thread_with_return_start(self):
        self.thread.start()
        self.assertEqual(self.thread.join(), self.thread_should_return)
