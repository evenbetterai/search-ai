from search_ai.ga.fitness.continuous_fitness import ContinuousFitness


class DumbContinuousFitness(ContinuousFitness):
    def __init__(self, features_info):
        super(DumbContinuousFitness, self).__init__(features_info)

    def run(self):
        return True
