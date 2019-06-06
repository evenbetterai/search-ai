import math
import random as rd

from ga.fitness.fitness import Fitness
from ga.individual.binary_individual import BinaryIndividual


class BinaryFitness(Fitness):

    def __init__(self, fitness_converter_list, run_params_dict):
        super(BinaryFitness,
              self).__init__(fitness_converter_list, run_params_dict)

    def features_to_fitness_els(self, individual):
        fitness_el_list = []
        ind_features = individual.features
        min_index = 0

        for conv_el in self._fitness_converter_list:
            params = []

            for el in conv_el[0]:
                params.append(int(ind_features[min_index:min_index + el]))
                min_index += el

            fitness_el_list.append(conv_el[1](params))

        return fitness_el_list

    def fitness_els_to_features(self):
        self._len_features = 0
        new_fit_conv_list = []

        for conv_el in self._fitness_converter_list:
            new_fit_conv_list.append([None for i in range(len(conv_el))])
            new_fit_conv_list[-1][0] = []
            new_fit_conv_list[-1][1] = conv_el[1]

            for el in conv_el[0]:
                new_fit_conv_list[-1][0].append(
                    int(math.log2(el[1] - el[0])) + 1
                )

                self._len_features += new_fit_conv_list[-1][0][-1]

        self._fitness_converter_list = new_fit_conv_list

    def new_empty_individual(self):
        return BinaryIndividual(self._len_features)

    def new_random_individual(self):
        ind = self.new_empty_individual()

        for i in range(len(ind.features)):
            ind.features[i] = rd.randint(0, 1)

        return ind
