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

        self._current_gen = 0
        self._population = None
        self.u = u # population size
        self.k = k # maximum lifetime
        self.h = h # produce h children
        self.p = p # number of parent that produce a child
        self._replace_duplicates = replace_dups
        self._elitism = elitism
        self._initialization = init
        self._selection = sel
        self._recombination = rec
        self._mutation = mut
        self._recombination_times = self._l // self._recombination.num_of_children
        self._recombination_times += 1 if self._l % self._recombination.num_of_children != 0 else 0

        if stop_crit is None:
            self._stop_criteria = lambda ga: ga.current_generation >= 100

    @property
    def current_generation(self):
        return self._current_gen

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
        return self._replace_dup

    @replace_duplicates.setter
    def replace_duplicates(self, replace_duplicates):
        self._replace_dup = replace_duplicates

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

        while not self._stop_crit():
            for _ in range(self._recombination_times):
                self._childs = []
                parents = self._selection.run(self._population)
                self._childs += self._recombination.run(parents)

            for child in self._childs:
                self._mutation.run(child)
                self._fitness.run(child)

            self.update_population()
            print(self._population[0])

    @property
    def u(self):
        return self._u

    @u.setter
    def u(self, u):
        if u < 2:
            raise ValueError('\'u\' attribute has to hold a number ' + \
                             ' greater or equal to \'2\'')

        self._u = u

    def update_population(self):
        self._current_gen += 1
        self._replace_dup.run(self._population, self._childs)
        self._population += self._childs
        self._population.sort(key=lambda ind: ind.fitness)
        self._elitism.run(self._population)

        for i in range(len(self._population) - 1, -1, -1):
            self._population[i].age += 1

            if self._population[i].age > self._k:
                self._population.pop(i)

        self._population = self._population[0:self._u]
