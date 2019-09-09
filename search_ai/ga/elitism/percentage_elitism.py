from search_ai.ga.elitism.elitism import Elitism


class PercentageElitism(Elitism):
    
    def __init__(self, k, elitism):
        super(PercentageElitism, self).__init__(k)
        self.elitism = elitism
    
    @property
    def elitism(self):
        return self._elitism
    
    @elitism.setter
    def elitism(self, elitism):
        if not 0 <= elitism <= 1:
            raise ValueError(
                '\'elitsim\' has to be a value between 0 and 1'
            )
        
        self._elitism = elitism
    
    def run(self, population, children):
        population_and_children = list(population) + list(children)
        
        for _ in range(int(self._elitism * len(population))):
            ind = max(population_and_children)
            
            if ind.age >= self._k - 1:
                ind.age = self._k - 2
            
            population_and_children.pop(
                population_and_children.index(ind)
            )
