import unittest
import unittest.mock as mock


class TestReplacers(object):

    class TestReplacer(unittest.TestCase):

        def setUp(self):
            self.fitness = mock.MagicMock()

        def check_replacer_attributes(self, replace_duplucates, fitness):
           self.assertIs(self.fitness, self.replacer.fitness)

        def test_replacer_fitness(self):
            self.assertIs(self.fitness, self.replacer.fitness)

            new_fitness = object()
            self.replacer.fitness = new_fitness
            self.assertIs(self.replacer.fitness, new_fitness)
