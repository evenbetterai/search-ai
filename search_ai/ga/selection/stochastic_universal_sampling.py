import random as rd

from search_ai.ga.selection.selection import Selection


class StochasticUniversalSampling(Selection):

    def __init__(self, num_of_parents=2):
        super(StochasticUniversalSampling,
              self).__init__(num_of_parents)

    # Algorithm assumes ind.fitness >= 0 for all ind in population
    def run(self, population):
        if len(population) == self._number_of_parents:
            return list(population)

        parents = []
        total_fitness = 0
        fitness_aux = 0
        i = 0

        for parent in population:
            total_fitness += parent.fitness

        fitness_step = total_fitness / self._number_of_parents
        random_value = rd.uniform(0, fitness_step)

        for _ in range(self._number_of_parents):
            fitness_aux += population[i].fitness

            while fitness_aux > random_value:
                parents.append(population[i])
                random_value += fitness_step

            i += 1

        return parents
