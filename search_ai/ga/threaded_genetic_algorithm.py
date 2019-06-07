from search_ai.ga.genetic_algorithm import GeneticAlgorithm
from utils.thread_with_return import ThreadWithReturn


class ThreadedGeneticAlgorithm(GeneticAlgorithm):

    @staticmethod
    def __chose_child(ga):
        child = ga._childs[ga._child_index]
        ga._child_index = (ga._child_index + 1) % len(ga._childs)
        return (child, )

    @staticmethod
    def __sel_rec_thread(ga):
        return ga.recombination.run(ga.selection.run(ga.population))

    @staticmethod
    def __mut_fit_thread(ga, child):
        ga.mutation.run(child)
        ga.fitness.run(child)
        return None

    def __init__(
            self,
            u,
            k,
            l,
            p,
            fitness,
            init,
            sel,
            rec,
            mut,
            rep_dup,
            elitism=0,
            stop_crit=None
    ):
        super(ThreadedGeneticAlgorithm, self).__init__(
            u, k, l, p, fitness, init, sel, rec, mut, rep_dup, elitism,
            stop_crit
        )

        self._child_index = 0

    def run(self):
        self._population = self._initialization.run()

        while not self._stop_crit(self):
            self._childs = []
            threads_list = ThreadWithReturn.create_and_start_threads(
                self._rec_times,
                ThreadedGeneticAlgorithm.__sel_rec_thread, lambda:
                (self, )
            )

            for thread in threads_list:
                self._childs += thread.join()

            threads_list = ThreadWithReturn.create_and_start_threads(
                self._l, ThreadedGeneticAlgorithm.__mut_fit_thread,
                ThreadedGeneticAlgorithm.__chose_child
            )

            for thread in threads_list:
                thread.join()

            self.update_population()

        print(self._population[0])
