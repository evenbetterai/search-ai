from search_ai.ga.initialization.initialization_component import InitializationComponent


class Initialization(object):

    def __init__(
            self, fitness, u, init_population_size, init_leafs=tuple()
    ):
        self.fitness = fitness
        self.u = u
        self.initialization_population_size = init_population_size
        self.initialization_leafs = init_leafs

    def check_repeated_ind(self, population):
        i = 0
        len_pop = len(population)

        while i < len_pop:
            cont = True

            for j in range(i + 1, len_pop):
                if population[i] == population[j]:
                    population[i] = self._fitness.new_random_individual(
                    )
                    cont = False
                    break

            if cont:
                i += 1

        return population

    @property
    def initialization_leafs(self):
        return self._initialization_leafs

    @initialization_leafs.setter
    def initialization_leafs(self, new_init_leafs_list):
        self._initialization_leafs = new_init_leafs_list

    @property
    def init_population_size(self):
        return self._init_population_size

    @init_population_size.setter
    def init_population_size(self, new_value):
        if new_value < self._u:
            raise ValueError('\'init_population_size\' attribute has to' + \
                             ' hold a number greater or equal to \'u\' ' + \
                             'attribute')

        self._init_population_size = new_value

    @property
    def fitness(self):
        return self._fitness

    @fitness.setter
    def fitness(self, new_fitness):
        self._fitness = new_fitness

    def run(self):
        population = []

        for _ in range(self._init_population_size):
            ind = self._fitness.new_random_individual()
            self._fitness.run(ind)
            population.append(ind)

        population = self.check_repeated_ind(population)

        for leaf in self._initialization_leafs:
            leaf.run(population)

        return population.sort(key=lambda ind: ind.fitness)[0:self._u]

    @property
    def u(self):
        return self._u

    @u.setter
    def u(self, new_value):
        if new_value < 2 or new_value > self._init_population_size:
            raise ValueError('\'u\' attribute has to hold a number ' + \
                             'between \'2\' and ' + \
                             '\'self.init_population_size')

        self._u = new_value
