import math

from ga.fitness.fitness import Fitness
from ga.initialization.initialization import Initialization
from ga.mutation.mutation import Mutation
from ga.recombination.recombination import Recombination
from ga.replace_duplicates.replace_duplicates import ReplaceDuplicates
from ga.selection.selection import Selection


class GeneticAlgorithm(object):

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
            replace_dup=False,
            elitism=0,
            stop_crit=None
    ):
        self._current_gen = 0
        self._population = None
        self.u = u
        self.k = k
        self.l = l
        self.p = p
        self.replace_duplicates = replace_dup
        self.elitism = int(self._u * elitism)
        self._fitness = fitness
        self._initialization = init
        self._selection = sel
        self._recombination = rec

        if self._l % self._recombination.num_of_children:
            raise ValueError('\'num_childs\' attribute of ' + \
                             '\'recombination\' has to be a divisor of ' + \
                             '\'self._l\'')

        self._rec_times = self._l // self._recombination.num_of_children
        self._mutation = mut

        if stop_crit is None:
            self._stop_crit = lambda ga: ga.current_generation >= 100

    @property
    def current_generation(self):
        return self._current_gen

    @property
    def fitness(self):
        return self._fitness

    @fitness.setter
    def fitness(self, new_fitness):
        self._fitness = new_fitness

    @property
    def elitism(self):
        return self._elitism

    @elitism.setter
    def elitism(self, new_value):
        if 0 > new_value or new_value >= self._u:
            raise ValueError('\'elitism\' attribute has to hold a number ' + \
                             'between [\'0\', \'u\') ')

        self._elitism = new_value

    @property
    def initialization(self):
        return self._initialization

    @initialization.setter
    def initialization(self, new_init):
        self._initialization = new_init

    @property
    def mutation(self):
        return self._mutation

    @mutation.setter
    def mutation(self, new_mutation):
        self._mutation = new_mutation

    @property
    def recombination(self):
        return self._recombination

    @recombination.setter
    def recombination(self, new_recombination):
        self._recombination = new_recombination

    @property
    def replace_duplicates(self):
        return self._replace_dup

    @replace_duplicates.setter
    def replace_duplicates(self, new_rep):
        self._replace_dup = new_rep

    @property
    def selection(self):
        return self._selection

    @selection.setter
    def selection(self, new_selection):
        self._selection = new_selection

    @property
    def k(self):
        return self._k

    @k.setter
    def k(self, new_value):
        if new_value < 1:
            raise ValueError('\'k\' attribute has to hold a number ' + \
                             'greater or equal to \'0\'')

        self._k = new_value

    @property
    def l(self):
        return self._l

    @l.setter
    def l(self, new_value):
        if new_value < 2:
            raise ValueError('\'l\' attribute has to hold a number ' + \
                             ' greater or equal to \'1\'')

        self._l = new_value

    @property
    def p(self):
        return self._p

    @p.setter
    def p(self, new_value):
        if new_value < 1:
            raise ValueError('\'p\' attribute has to hold a number ' + \
                             ' greater or equal to \'1\'')

        self._p = new_value

    @property
    def population(self):
        return self._population

    @population.setter
    def population(self, new_pop):
        self._population = new_pop

    def run(self):
        self._population = self._initialization.run()

        while not self._stop_crit(self):
            for _ in range(self._rec_times):
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
    def u(self, new_value):
        if new_value < 2:
            raise ValueError('\'u\' attribute has to hold a number ' + \
                             ' greater or equal to \'2\'')

        self._u = new_value

    def update_population(self):
        self._current_gen += 1
        self._replace_dup.run(self._population, self._childs)
        self._population += self._childs
        self._population.sort(key=lambda ind: ind.fitness)
        self._elite = self._population[0:self._elitism]

        # remove individuals with max age and not in 'self._elite'
        for i in range(self._population):
            individual = self._population[i]
            individual.age += 1

            if individual not in self._elite and individual.age > self._k:
                del self._population[i]

        self._population = self._population[0:self._u]
