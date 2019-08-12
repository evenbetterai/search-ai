import random as rd

from search_ai.ga.mutation.mutation import Mutation


class StandardBinaryMutation(Mutation):

    def __init__(self, mut_prob):
        super(StandardBinaryMutation, self).__init__(mut_prob)

    def mutate(self, child, index):
        child.set_feature_at(index, not child.get_feature_at(index))
