class Search(object):
    
    @staticmethod
    def sequencial_search(iterable, el, key=lambda el: el):
        i = -1
        
        for iter_el in iterable:
            i += 1
            
            if key(el) == key(iter_el):
                return i
        
        return -1
    
    @staticmethod
    def binary_search(sequence, el, key=lambda el: el):
        low = 0
        high = len(sequence) - 1
        current = high // 2
        
        if high < low:
            return -1
        
        elif high == low:
            return low if key(el) == key(sequence[low]) else -1
        
        else:
            return Search._binary_search_cycle(
                sequence,
                el,
                key,
                current,
                low,
                high
            )
    
    @staticmethod
    def _binary_search_cycle(sequence, el, key, current, low, high):
        while low <= high:
            if key(el) == key(sequence[current]):
                return current
            
            elif key(el) > key(sequence[current]):
                low = current + 1
            
            else:
                high = current - 1
            
            current = (high-low) // 2 + low
        
        return -1
