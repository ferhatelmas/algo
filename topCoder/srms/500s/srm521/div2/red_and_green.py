from sys import maxint

class RedAndGreen:
    def minPaints(self, row):
        r, c, l = maxint, 0, len(row)
        for i in xrange(l+1):
            r = min(r, c + sum(e == 'R' for e in row[i:]))
            c += (i < l and row[i] == 'G')
        return r
