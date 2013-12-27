class ContiguousSubsequences:
    def findMaxAverage(self, a, K):
        def avg(ls):
            return sum(ls) / float(len(ls))
        l, m, mi, mj = len(a), -1, 0, 0
        for i in xrange(l, K-1, -1):
            for j in xrange(l-i+1):
                g = avg(a[j:j+i])
                if g > m:
                    m = g
                    mi = j
                    mj = i+j-1
        return mi, mj
