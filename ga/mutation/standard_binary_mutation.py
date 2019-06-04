import random as rd

from ga.mutation.mutation import Mutation

class StandardBinaryMutation(Mutation):
  def __init__(self, mut_prob):
    super(StandardBinaryMutation, self).__init__(mut_prob)

  def mutation(self, child, index):
    return not child.features[index]
