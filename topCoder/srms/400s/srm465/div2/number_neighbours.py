from itertools import groupby

class NumberNeighbours:
    def numPairs(self, numbers):
        def f(n):
            return int(''.join(sorted(str(n))))
        return sum(map(lambda n: n*(n-1)/2 if n > 1 else 0,
                       (len(list(g)) for _, g in groupby(sorted(map(f, numbers))))))
