from itertools import groupby


class MonotoneSequence:
    def longestMonotoneSequence(self, seq):
        m = 1
        for k, g in groupby([cmp(seq[i - 1], seq[i]) for i in xrange(1, len(seq))]):
            if k in [-1, 1]:
                m = max(m, len(list(g)) + 1)
        return m
