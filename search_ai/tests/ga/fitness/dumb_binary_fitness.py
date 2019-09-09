from search_ai.ga.fitness.binary_fitness import BinaryFitness


class DumbBinaryFitness(BinaryFitness):
    
    def __init__(self, len_features):
        super(DumbBinaryFitness, self).__init__(len_features)
    
    def run(self):
        return True
