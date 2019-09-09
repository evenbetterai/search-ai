from search_ai.ga.fitness_holder import FitnessHolder


class GeneticAlgorithm(FitnessHolder):
    
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
            replace_dups,
            elitism,
            stop_crit=None
    ):
        super(GeneticAlgorithm, self).__init__(fitness)
        
        self._current_generation = 0
        self._population = None
        self.u = u    # population size
        self.k = k    # maximum lifetime
        self.h = h    # produce h children
        self.p = p    # number of parent that produce a child
        self.replace_duplicates = replace_dups
        self.elitism = elitism
        self.initialization = init
        self.selection = sel
        self.recombination = rec
        self.mutation = mut
        self._recombination_times = self.h // self._recombination.number_of_children
        self._recombination_times += 1 if self.h % self._recombination.number_of_children != 0 else 0
        
        if stop_crit is None:
            self._stop_criteria = lambda ga: ga.current_generation >= 100
        else:
            self._stop_criteria = stop_crit
    
    @property
    def current_generation(self):
        return self._current_generation
    
    @property
    def elitism(self):
        return self._elitism
    
    @elitism.setter
    def elitism(self, elitism):
        self._elitism = elitism
    
    @property
    def initialization(self):
        return self._initialization
    
    @initialization.setter
    def initialization(self, initialization):
        self._initialization = initialization
    
    @property
    def mutation(self):
        return self._mutation
    
    @mutation.setter
    def mutation(self, mutation):
        self._mutation = mutation
    
    @property
    def recombination(self):
        return self._recombination
    
    @recombination.setter
    def recombination(self, recombination):
        self._recombination = recombination
    
    @property
    def replace_duplicates(self):
        return self._replace_duplicates
    
    @replace_duplicates.setter
    def replace_duplicates(self, replace_duplicates):
        self._replace_duplicates = replace_duplicates
    
    @property
    def selection(self):
        return self._selection
    
    @selection.setter
    def selection(self, selection):
        self._selection = selection
    
    @property
    def k(self):
        return self._k
    
    @k.setter
    def k(self, k):
        if k < 1:
            raise ValueError('\'k\' attribute has to hold a number ' + \
                             'greater or equal to \'0\'')
        
        self._k = k
    
    @property
    def h(self):
        return self._h
    
    @h.setter
    def h(self, h):
        if h < self.u:
            raise ValueError('\'h\' attribute has to hold a number ' + \
                             ' greater or equal to \'u\' attribute')
        
        self._h = h
    
    @property
    def p(self):
        return self._p
    
    @p.setter
    def p(self, p):
        if p < 1:
            raise ValueError('\'p\' attribute has to hold a number ' + \
                             ' greater or equal to \'1\'')
        
        self._p = p
    
    @property
    def population(self):
        return self._population
    
    def run(self):
        self._population = self._initialization.run()
        
        while not self._stop_criteria(self):
            self._main_cicle()
    
    @property
    def u(self):
        return self._u
    
    @u.setter
    def u(self, u):
        if u < 2:
            raise ValueError('\'u\' attribute has to hold a number ' + \
                             ' greater or equal to \'2\'')
        
        self._u = u
    
    def _main_cicle(self):
        self._children = []
        
        for _ in range(self._recombination_times):
            parents = self._selection.run(self._population)
            self._children += self._recombination.run(parents)
        
        for child in self._children:
            self._mutation.run(child)
            self._fitness.run(child)
        
        self.update_population()
        print(self._population[0])
    
    def update_population(self):
        self._current_generation += 1
        self._replace_duplicates.run(self._population, self._children)
        self._elitism.run(self._population)
        
        for i in range(len(self._population) - 1, -1, -1):
            self._population[i].age += 1
            
            if self._population[i].age >= self._k:
                self._population.pop(i)
        
        self._population = sorted(
            self._population + self._children,
            reverse=True
        )[0:self.u]
