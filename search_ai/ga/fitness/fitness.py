from abc import ABC, abstractmethod


class Fitness(ABC):

    def __init__(self, fitness_converter_list, run_params_dict):
        self._fitness_converter_list = fitness_converter_list
        self._run_params_dict = run_params_dict
        self.fitness_els_to_features()

    @abstractmethod
    def features_to_fitness_els(self, individual):
        pass

    @abstractmethod
    def fitness_els_to_features(self):
        pass

    @abstractmethod
    def new_blank_individual(self):
        pass

    @abstractmethod
    def new_random_individual(self):
        pass

    @abstractmethod
    def run(self, individual):
        pass
