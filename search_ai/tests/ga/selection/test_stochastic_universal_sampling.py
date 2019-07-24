from search_ai.ga.selection.stochastic_universal_sampling import StochasticUniversalSampling
from search_ai.ga.individual.binary_individual import BinaryIndividual

from search_ai.tests.ga.selection.test_selection import TestSelection


class TestStochasticUniversalSampling(TestSelections.TestSelection):
    def setUp(self):
        super(TestStochasticUniversalSampling, self).setUp()
        self.selection = StochasticUniversalSampling(self.number_of_parents)

        self.oneIndividual = [BinaryIndividual(5) for _ in range(1)]
        self.oneIndividual[0].fitness = 1

        self.twoIndividuals = [BinaryIndividual(5) for _ in range(2)]
        self.twoIndividuals[0].fitness = 1
        self.twoIndividuals[1].fitness = 1

        self.fiveIndividuals = [BinaryIndividual(5) for _ in range(5)]
        self.fiveIndividuals[0].fitness = 1
        self.fiveIndividuals[1].fitness = 0.1
        self.fiveIndividuals[2].fitness = 0.1
        self.fiveIndividuals[3].fitness = 0.1
        self.fiveIndividuals[4].fitness = 0.1

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
        pop = self.selection.run(self.oneIndividual)
        self.check_len_array_and_reference(pop, [self.oneIndividual[0] for _ in range(3)], 3)

        pop = self.selection.run(self.twoIndividuals)
        self.check_at_least_reference(pop, self.twoIndividuals[0], 1)
        self.check_at_least_reference(pop, self.twoIndividuals[1], 1)

        self.selection.number_of_parents = 10
        pop = self.selection.run(self.fiveIndividuals)
        self.check_at_least_reference(pop, self.fiveIndividuals[0], 8)


    def check_len_array_and_reference(self, returned, expected, expected_len):
        self.assertEquals(len(returned), expected_len)

        for i in range(expected_len):
            self.assertTrue(returned[i] is expected[i])

    def check_at_least_reference(self, returned, expected, min_times):
        n_times = 0
        for ind in returned:
            if returned is expected:
                n_times += 1

        self.assertTrue(n_times >= min_times)

