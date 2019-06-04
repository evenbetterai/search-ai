import random as rd

from ga.selection.selection import Selection

class TournamentSelection(Selection):
  def __init__(self, num_of_parents=2, tournament_size=2):
    super(TournamentSelection, self).__init__(num_of_parents)
    self._tournament_size = tournament_size

  def run(self, population):
    parents = []

    for _ in range(self._number_of_parents):
      parents.append(
        max(rd.choices(population, k=self._tournament_size), 
            key=lambda ind: ind.fitness))

    return parents
