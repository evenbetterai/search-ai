from search_ai.ga.recombination.global_uniform_crossover import GlobalUniformCrossover
from search_ai.ga.individual.binary_individual import BinaryIndividual

from search_ai.tests.ga.recombination.test_recombination import TestRecombinations


class TestGlobalUniformCrossover(TestRecombinations.TestRecombination):

    def set_all_individuals_features(self, individuals, value):
        for ind in individuals:
            for i in range(len(ind.features)):
                ind.features[i] = value

    def setUp(self):
        super(TestGlobalUniformCrossover, self).setUp()
        self.set_up_fitness(self.number_of_children, 3)
        self.recombination = GlobalUniformCrossover(self.fitness, self.number_of_children)

    def test_global_uniform_crossover_constructor(self):
        self.check_recombination_attributes(self.recombination, self.number_of_children)
        rec = GlobalUniformCrossover(self.fitness, 1)
        self.check_recombination_attributes(rec, 1)

    def test_recombination_constructor_exception(self):
        with self.assertRaises(Exception):
            GlobalUniformCrossover(None, 2)
            GlobalUniformCrossover(self.fitness, 0)

    def test_global_uniform_crossover_run(self):            
        parents = [BinaryIndividual(self.len_features) for _ in range(3)]
        children_to_compare = [BinaryIndividual(self.len_features) for _ in range(self.number_of_children)]
        children = self.recombination.run(parents)
        self.cmp_arrays(children, children_to_compare)

        self.set_all_individuals_features(parents, 1)
        self.set_all_individuals_features(children_to_compare, 1)
        children = self.recombination.run(parents)
        self.cmp_arrays(children, children_to_compare)

        self.set_all_individuals_features(parents, 0)
        diff_index = 0
        parents[1].set_feature_at(diff_index, 1)
        children = self.recombination.run(parents)

        for child in children:
            for i in range(self.len_features):
                if i == diff_index:
                    self.assertTrue(child.features[i] == 0 or child.features[i] == 1)

                else:
                    self.assertEqual(child.features[i], parents[0].features[i])
