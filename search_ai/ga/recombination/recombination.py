from abc import abstractmethod

from search_ai.ga.fitness_holder import FitnessHolder


class Recombination(FitnessHolder):
    
    def __init__(self, fitness, num_of_children):
        super(Recombination, self).__init__(fitness)
        self.number_of_children = num_of_children
    
    @property
    def number_of_children(self):
        return self._number_of_children
    
    @number_of_children.setter
    def number_of_children(self, new_value):
        if new_value < 1:
            raise ValueError('\'num_of_children\' attribute has to hold' + \
                             'a number greater or equal to \'1\'')
        
        self._number_of_children = new_value
    
    @abstractmethod
    def run(self, parents):
        pass
