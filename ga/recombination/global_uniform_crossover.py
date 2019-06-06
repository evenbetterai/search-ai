import random as rd

from ga.recombination.recombination import Recombination


class GlobalUniformCrossover(Recombination):

    def __init__(self, fitness, num_of_children):
        super(GlobalUniformCrossover,
              self).__init__(fitness, num_of_children)

    def run(self, parents):
        children = []

        for _ in range(self._number_of_children):
            child = self._fitness.new_empty_individual()

            for i in range(len(child.features)):
                child.feature[i] = rd.choice(parents).feature[i]

            children.append(child)

        return children
