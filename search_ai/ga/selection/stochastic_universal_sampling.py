import random as rd

from search_ai.ga.selection.selection import Selection


class StochasticUniversalSampling(Selection):

    def __init__(self, num_of_parents=2):
        super(StochasticUniversalSampling,
              self).__init__(num_of_parents)

    # Algorithm assumes ind.fitness >= 0 for all ind in population
    def run(self, population):
        parents = []
        fitness_aux = 0
        i = rd.randint(0, len(population) - 1)

        fitness_step = self._sum_of_population_fitness(population) / self._number_of_parents
        random_value = rd.uniform(0, fitness_step)

        while len(parents) < self._number_of_parents:
            fitness_aux += population[i].fitness
            random_value = self._add_chosen_individual(parents, population[i], fitness_step, fitness_aux, random_value)
            i = (i + 1) % len(population)

        return parents

    def _sum_of_population_fitness(self, population):
        s = 0

        for individual in population:
            s += individual.fitness

        return s

    def _add_chosen_individual(self, parents, individual, fitness_step, fitness_aux, random_value):
        while fitness_aux > random_value:
            parents.append(individual)
            random_value += fitness_step

        return random_value
