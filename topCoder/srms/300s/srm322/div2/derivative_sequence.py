class DerivativeSequence:
    def derSeq(self, a, n):
        def seq(ns):
            return [ns[i+1] - ns[i] for i in xrange(len(ns)-1)]
        for _ in xrange(n):
            a = seq(a)
        return a
