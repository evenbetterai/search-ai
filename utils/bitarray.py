from bitarray import bitarray

class BitArray(bitarray):
    def __str__(self):
        return self.to01()

    def __int__(self):
        return int(self.to01(), 2)
