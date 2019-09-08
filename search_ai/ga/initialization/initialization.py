from search_ai.ga.fitness_holder import FitnessHolder


class Initialization(FitnessHolder):

    def __init__(self, u, init_population_size, fitness, replace_duplicates):
        super(Initialization, self).__init__(fitness)

        self._init_population_size = init_population_size
        self.u = u
        self.init_population_size = init_population_size
        self.fitness = fitness
        self.replace_duplicates = replace_duplicates

    @property
    def init_population_size(self):
        return self._init_population_size

    @init_population_size.setter
    def init_population_size(self, init_population_size):
        if init_population_size < self._u:
            raise ValueError('\'init_population_size\' attribute has to' + \
                             ' hold a number greater or equal to \'u\' ' + \
                             'attribute')

        self._init_population_size = init_population_size

    @property
    def replace_duplicates(self):
        return self._replace_duplicates

    @replace_duplicates.setter
    def replace_duplicates(self, replace_duplicates):
        self._replace_duplicates = replace_duplicates

    def run(self):
        population = []

        for _ in range(self._init_population_size):
            ind = self._fitness.new_random_individual()
            self._fitness.run(ind)
            population.append(ind)

        self._replace_duplicates.run(population)
        return sorted(population, reverse=True)[0:self._u]

    @property
    def u(self):
        return self._u

    @u.setter
    def u(self, u):
        if u < 2 or u > self._init_population_size:
            raise ValueError('\'u\' attribute has to hold a number ' + \
                             'between \'2\' and ' + \
                             '\'self.init_population_size')

        self._u = u
