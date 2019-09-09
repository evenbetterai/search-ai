from search_ai.ga.replace_duplicates.replacer.replacer import Replacer


class RandomReplacer(Replacer):
    
    def __init__(self, fitness):
        super(RandomReplacer, self).__init__(fitness)
    
    def get_new_individual(self):
        new_child = self._fitness.new_random_individual()
        self._fitness.run(new_child)
        return new_child
    
    def replace_in_population(self, replace_duplicates, index):
        replace_duplicates._population[index] = self.get_new_individual(
        )
    
    def replace_in_children(self, replace_duplicates, index):
        replace_duplicates._children[index] = self.get_new_individual()
