from abc import ABC, abstractmethod
import random as rd


class Mutation(ABC):

    def __init__(self, mut_prob):
        self._mut_prob = mut_prob

    @property
    def mut_prob(self):
        return self._mut_prop

    @mut_prob.setter
    def mut_prob(self, new_value):
        if 0 <= new_value <= 1:
            self._mut_prop = new_value

        else:
            raise ValueError('\'mut_prob\' attribute has to hold a ' + \
                             'number between \'0\' and \'1\'')

    def run(self, child):
        for i in range(len(child.features)):
            if rd.random() < self._mut_prob:
                child.features[i] = self.mutation(child, i)

    @abstractmethod
    def mutation(self, child, index):
        pass
