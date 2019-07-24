from abc import ABC, abstractmethod


class Selection(ABC):

    MIN_NUMBER_OF_PARENTS = 2

    def __init__(self, num_of_parents):
        self._number_of_parents = num_of_parents
        self.number_of_parents = num_of_parents

    @property
    def number_of_parents(self):
        return self._number_of_parents

    @number_of_parents.setter
    def number_of_parents(self, number_of_parents):
        if self._number_of_parents < Selection.MIN_NUMBER_OF_PARENTS:
            raise ValueError("'number_of_parents' should be greater than " + str(Selection.MIN_NUMBER_OF_PARENTS))

        self._number_of_parents = number_of_parents

    @abstractmethod
    def run(self, population):
        pass
