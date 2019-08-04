class Search(object):

    @staticmethod
    def sequencial_search(iterable, el, key = lambda el: el):
        i = -1

        for iter_el in iterable:
            i += 1

            if key(el) == key(iter_el):
                return i

        return -1

    @staticmethod
    def binary_search(sequence, el, key = lambda el: el):
        low = 0
        high = len(sequence) - 1
        current = high // 2

        while low < high:
            if key(el) == key(sequence[current]):
                return current
            
            elif key(el) > key(sequence[current]):
                low = current + 1

            else:
                high = current - 1

            current = (high - low) // 2 + low
        
        return low if high >= 0 and key(el) == key(sequence[low]) else -1
