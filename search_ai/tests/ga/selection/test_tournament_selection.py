from search_ai.ga.selection.tournament_selection import TournamentSelection
from search_ai.ga.individual.binary_individual import BinaryIndividual

from search_ai.tests.ga.selection.test_selection import TestSelections


class TestStochasticUniversalSampling(TestSelections.TestSelection):
    def setUp(self):
        super(TestStochasticUniversalSampling, self).setUp()
        self.min_tournament_size = 1
        self.tournament_size = 8
        self.selection = TournamentSelection(self.number_of_parents, self.tournament_size)

    def test_tournament_selection_constructor(self):
        self.check_selection_attributes()
        self.assertEqual(self.selection.tournament_size, self.tournament_size)

        sus = TournamentSelection()
        self.assertEqual(sus.number_of_parents, self.min_number_of_parents)
        self.assertEqual(sus.tournament_size, self.min_tournament_size)

    def test_tournament_selection_constructor_exception(self):
        with self.assertRaises(ValueError):
            TournamentSelection(1)
            TournamentSelection(2, 0)
            TournamentSelection(2, -10)

    def test_tournament_selection_run(self):
        self.selection.tournament_size = 1
        self.selection.number_of_parents = 2
        pop = self.selection.run(self.one_individual)
        self.check_len_array_and_reference(pop, [self.one_individual[0] for _ in range(self.selection.number_of_parents)])

        self.selection.tournament_size = 2
        self.selection.number_of_parents = 4
        self.two_individuals[1].fitness = 0.1
        pop = self.selection.run(self.two_individuals)
        self.check_len_array_and_reference(pop, [self.two_individuals[0] for _ in range(self.selection.number_of_parents)])

        self.selection.tournament_size = 4
        self.selection.number_of_parents = 10
        self.five_individuals[4].fitness = 0.001
        pop = self.selection.run(self.five_individuals)
        self.check_reference_at_most_n_times(pop, self.five_individuals[4], 0)

    def check_len_array_and_reference(self, returned, expected):
        self.assertEqual(len(returned), len(expected))

        for i in range(len(expected)):
            self.assertIs(returned[i], expected[i])

    def check_reference_at_least_n_times(self, returned, expected, min_times):
        n_times = 0
        for ind in returned:
            if ind is expected:
                n_times += 1

        self.assertGreaterEqual(n_times, min_times)

    def check_reference_at_most_n_times(self, returned, expected, max_times):
        n_times = 0
        for ind in returned:
            if ind is expected:
                n_times += 1

        self.assertLessEqual(n_times, max_times)

