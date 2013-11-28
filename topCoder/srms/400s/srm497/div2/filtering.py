from operator import itemgetter
from sys import maxint

class Filtering:
    def designFilter(self, sizes, outcome):
        m, n = -maxint-1, maxint
        for s, o in sorted(zip(sizes, outcome), key=itemgetter(1, 0)):
            if o == 'A':
                m = max(m, s)
                n = min(n, s)
            elif m >= s >= n:
                return []
        return [] if n == maxint else [n, m]
