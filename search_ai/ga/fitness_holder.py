from abc import ABC


class FitnessHolder(ABC):
    """Simple base class to hold a fitness.fitness.Fitness object.

    Note
    ----
    No validations are performed to check if the passed object extends
    from fitness.fitness.Fitness.

    See Also
    --------
    fitness : Fitness sub-module.

    """
    
    def __init__(self, fitness):
        """Initialize FitnessHolder, by storing `fitness`.

        Parameters
        ----------
        fitness : fitness.fitness.Fitness
            Object to hold.

        """
        self._fitness = fitness
    
    @property
    def fitness(self):
        """fitness.fitness.Fitness: Get or set object being hold."""
        return self._fitness
    
    @fitness.setter
    def fitness(self, fitness):
        self._fitness = fitness
