from itertools import combinations
from sys import maxint

class HammingDistance:
    def minDistance(self, numbers):
        def c(a, b):
            return sum(map(lambda (x, y): 0 if x == y else 1, zip(a, b)))
        m = maxint
        for a, b in combinations(numbers, 2):
            m = min(m, c(a, b))
        return m
