class InsertionSortCount:
    def countMoves(self, A):
        r, s = [], 0
        for i, e in enumerate(A):
            c = i
            for j in xrange(i-1, -1, -1):
                if r[j] > e:
                    c -= 1
            r.insert(c, e)
            s += i-c
        return s
