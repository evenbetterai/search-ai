class Initialization(object):

    def __init__(self, u, init_population_size, fitness, rep_dup):
        self._init_population_size = init_population_size
        self.u = u
        self.init_population_size = init_population_size
        self.fitness = fitness
        self.replace_duplicates = rep_dup

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

    @property
    def replace_duplicates(self):
        return self._replace_duplicates

    @replace_duplicates.setter
    def replace_duplicates(self, new_rep_dup):
        self._replace_duplicates = new_rep_dup

    def run(self):
        children = []

        for _ in range(self._init_population_size):
            ind = self._fitness.new_random_individual()
            self._fitness.run(ind)
            children.append(ind)
            self._replace_duplicates([], children)

        return children.sort(reverse=True)[0:self._u]

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
