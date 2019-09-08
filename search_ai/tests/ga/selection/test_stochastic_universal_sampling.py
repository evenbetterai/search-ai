from search_ai.ga.selection.stochastic_universal_sampling import StochasticUniversalSampling

from search_ai.tests.ga.selection.test_selection import TestSelections


class TestStochasticUniversalSampling(TestSelections.TestSelection):
    def setUp(self):
        super(TestStochasticUniversalSampling, self).setUp()
        self.selection = StochasticUniversalSampling(self.number_of_parents)

    def test_stochastic_universal_sampling_constructor(self):
        self.check_selection_attributes()

        sus = StochasticUniversalSampling()
        self.assertEqual(sus.number_of_parents, 2)

        sus = StochasticUniversalSampling(12)
        self.assertEqual(sus.number_of_parents, 12)

    def test_stochastic_universal_sampling_constructor_exception(self):
        with self.assertRaises(ValueError):
            StochasticUniversalSampling(1)
            StochasticUniversalSampling(-10)

    def test_stochastic_universal_sampling_run(self):
        pop = self.selection.run(self.one_individual)
        self.cmp_arrays(pop, [self.one_individual[0] for _ in range(3)], self.el1_is_el2)

        pop = self.selection.run(self.two_individuals)
        self.assertEqual(len(pop), self.number_of_parents)
        self.assertGreaterEqual(self.el_in_array(pop, self.two_individuals[0]), 1)
        self.assertGreaterEqual(self.el_in_array(pop, self.two_individuals[1]), 1)

        self.selection.number_of_parents = 10
        pop = self.selection.run(self.five_individuals)
        self.assertEqual(len(pop), 10)
        self.assertGreaterEqual(self.el_in_array(pop, self.five_individuals[0]), 7)
