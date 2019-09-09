import random as rd

from search_ai.ga.selection.selection import Selection


class TournamentSelection(Selection):
    
    MIN_TOURNAMENT_SIZE = 1
    
    def __init__(self, num_of_parents=2, tournament_size=1):
        super(TournamentSelection, self).__init__(num_of_parents)
        self.tournament_size = tournament_size
    
    @property
    def tournament_size(self):
        return self._tournament_size
    
    @tournament_size.setter
    def tournament_size(self, tournament_size):
        if tournament_size < TournamentSelection.MIN_TOURNAMENT_SIZE:
            raise ValueError(
                '\'tournament_size\' should not be less than \'' +
                TournamentSelection.MIN_TOURNAMENT_SIZE + '\''
            )
        
        self._tournament_size = tournament_size
    
    def run(self, population):
        parents = []
        
        for _ in range(self._number_of_parents):
            parents.append(
                max(rd.sample(population,
                              k=self._tournament_size))
            )
        
        return parents
