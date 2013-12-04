class Bits:
    def minBits(self, n):
        return len('{0:b}'.format(n))
