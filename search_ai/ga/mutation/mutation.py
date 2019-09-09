from abc import ABC, abstractmethod
import random as rd


class Mutation(ABC):
    
    def __init__(self, mutation_prob):
        self.mutation_prob = mutation_prob
    
    @property
    def mutation_prob(self):
        return self._mutation_prob
    
    @mutation_prob.setter
    def mutation_prob(self, new_value):
        if 0 <= new_value <= 1:
            self._mutation_prob = new_value
        
        else:
            raise ValueError('\'mutation_prob\' attribute has to hold a ' + \
                             'number between \'0\' and \'1\'')
    
    def run(self, child):
        for i in range(child.len_features()):
            if rd.random() < self._mutation_prob:
                self.mutate(child, i)
    
    @abstractmethod
    def mutate(self, child, index):
        pass
