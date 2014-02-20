from itertools import combinations

class AverageAverage:
    def average(self, numList):
        return sum(sum(c) / float(i) for i in xrange(1, len(numList)+1)
                   for c in combinations(numList, i)) / (2**len(numList)-1.0)
