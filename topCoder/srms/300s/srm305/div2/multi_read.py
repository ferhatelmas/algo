from itertools import groupby
from math import ceil

class MultiRead:
    def minCycles(self, trace, procs):
        c = 0
        for k, g in groupby(trace):
            if k == 'R':
                c += int(ceil(float(len(list(g))) / procs))
            else:
                c += len(list(g))
        return c
