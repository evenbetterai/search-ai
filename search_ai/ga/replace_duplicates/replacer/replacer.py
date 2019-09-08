from abc import abstractmethod

from search_ai.ga.fitness_holder import FitnessHolder


class Replacer(FitnessHolder):

    def __init__(self, fitness):
        super(Replacer, self).__init__(fitness)

    @abstractmethod
    def get_new_individual(self):
        pass

    @abstractmethod
    def replace_in_population(self, replace_duplicates):
        pass

    @abstractmethod
    def replace_in_children(self, replace_duplicates):
        pass

