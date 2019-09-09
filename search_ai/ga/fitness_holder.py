from abc import ABC


class FitnessHolder(ABC):
    
    def __init__(self, fitness):
        self._fitness = fitness
    
    @property
    def fitness(self):
        return self._fitness
    
    @fitness.setter
    def fitness(self, fitness):
        self._fitness = fitness
