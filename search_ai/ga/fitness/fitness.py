from abc import ABC, abstractmethod


class Fitness(ABC):
    
    MIN_FEATURES = 1
    
    def __init__(self, len_features):
        self.len_features = len_features
    
    @property
    def len_features(self):
        return self._len_features
    
    @len_features.setter
    def len_features(self, len_features):
        if len_features < Fitness.MIN_FEATURES:
            raise ValueError(
                '\'len_features\' should not be less than \'' +
                str(Fitness.MIN_FEATURES) + '\''
            )
        
        self._len_features = len_features
    
    @abstractmethod
    def new_blank_individual(self):
        pass
    
    @abstractmethod
    def new_random_individual(self):
        pass
    
    @abstractmethod
    def run(self, individual):
        pass
