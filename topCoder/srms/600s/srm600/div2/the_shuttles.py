from math import ceil
from sys import maxint

class TheShuttles:
    def getLeastCost(self, cnt, baseCost, seatCost):
        m = maxint
        for i in xrange(1, max(cnt)+1):
            cost = 0
            for c in cnt:
                cost += int(ceil(float(c) / i)) * (baseCost + seatCost * i)
            m = min(m, cost)
        return m
