from search_ai.ga.genetic_algorithm import GeneticAlgorithm
from search_ai.utils.thread_with_return import ThreadWithReturn


class ThreadedGeneticAlgorithm(GeneticAlgorithm):
    
    @staticmethod
    def _sel_rec_thread(ga):
        return ga.recombination.run(ga.selection.run(ga.population))
    
    @staticmethod
    def _mut_fit_thread(ga, child):
        ga.mutation.run(child)
        ga.fitness.run(child)
        return None
    
    def __init__(
            self,
            u,
            k,
            h,
            p,
            fitness,
            init,
            sel,
            rec,
            mut,
            rep_dup,
            elitism,
            stop_crit=None
    ):
        super(ThreadedGeneticAlgorithm,
              self).__init__(
                  u,
                  k,
                  h,
                  p,
                  fitness,
                  init,
                  sel,
                  rec,
                  mut,
                  rep_dup,
                  elitism,
                  stop_crit
              )
    
    def _main_cicle(self):
        self._children = []
        threads_list = ThreadWithReturn.create_and_start_threads(
            self._recombination_times,
            ThreadedGeneticAlgorithm._sel_rec_thread,
            ((self,
              ),
             ) * self._recombination_times
        )
        
        for thread in threads_list:
            self._children += thread.join()
        
        children_tuple = tuple()
        
        for child in self._children:
            children_tuple += ((self, child), )
        
        threads_list = ThreadWithReturn.create_and_start_threads(
            len(self._children),
            ThreadedGeneticAlgorithm._mut_fit_thread,
            children_tuple
        )
        
        for thread in threads_list:
            thread.join()
        
        self.update_population()
        print(self._population[0])
