class MinDifference:
    def closestElements(self, A0, X, Y, M, n):
        i, ls = 1, [A0]
        while i < n:
            ls.append((ls[-1] * X + Y)%M)
            i += 1
        ls.sort()
        return min([abs(ls[j-1]-ls[j]) for j in xrange(1, n)])
