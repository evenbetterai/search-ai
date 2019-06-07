from search_ai.ga.initialization.initialization import Initialization
from utils.thread_with_return import ThreadWithReturn


class ThreadedInitialization(Initialization):

    @staticmethod
    def create_individual_and_run_fitness(fitness):
        ind = fitness.new_random_individual()
        fitness.run(ind)
        return ind

    def __init__(
            self, fitness, u, init_population_size, init_leafs=list()
    ):
        super(ThreadedInitialization, self
              ).__init__(fitness, u, init_population_size, init_leafs)

    def run(self):
        population = []
        threads_list = ThreadWithReturn.create_and_start_threads(
            self._init_population_size,
            ThreadedInitialization.create_individual_and_run_fitness,
            lambda: (self.fitness, )
        )

        for thread in threads_list:
            population.append(thread.join())

        for leaf in self._initialization_leafs:
            leaf.run(population)

        return sorted(population)[0:self._u]
