import functools as ft


@ft.total_ordering
class ContinuousParameterInfo(object):
    '''
    Hold a number in a specific  domain.
    '''

    def __init__(self, min_value=0, max_value=100):
        self._min_value = min_value
        self.max_value = max_value

    def __eq__(self, other):
        return min_value == other.min_value and max_value == other.max_value

    def __le__(self, other):
        return min_value < other.min_value or min_value == other.min_value and max_value < other.max_value

    @property
    def min_value(self):
        return self._min_value

    @min_value.setter
    def min_value(self, new_value):
        if new_value < self._max_value:
            self._min_value = new_value

        else:
            raise ValueError('\'min_value\' attribute has to hold a ' + \
                             'number less than \'' + \
                             str(self._max_value) + '\'')

    @property
    def max_value(self):
        return self._max_value

    @max_value.setter
    def max_value(self, new_value):
        if new_value > self._min_value:
            self._max_value = new_value

        else:
            raise ValueError('\'max_value\' attribute has to hold a ' + \
                             'number greater than \'' + \
                             str(self._min_value) + '\'')
