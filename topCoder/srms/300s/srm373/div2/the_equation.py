class TheEquation:
    def leastSum(self, X, Y, P):
        m = 2*P
        for i in xrange(1, P+1):
            for j in xrange(1, P+1):
                if (X*i + Y*j)%P == 0:
                    m = min(m, i+j)
        return m
