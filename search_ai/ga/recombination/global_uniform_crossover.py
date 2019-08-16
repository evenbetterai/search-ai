import random as rd

from search_ai.ga.recombination.recombination import Recombination


class GlobalUniformCrossover(Recombination):

    def __init__(self, fitness, num_of_children):
        super(GlobalUniformCrossover,
              self).__init__(fitness, num_of_children)

    def run(self, parents):
        children = []

        for _ in range(self._number_of_children):
            child = self._fitness.new_blank_individual()

            for i in range(child.len_features()):
                child.set_feature_at(i, rd.choice(parents).get_feature_at(i))

            children += [child]

        return children
