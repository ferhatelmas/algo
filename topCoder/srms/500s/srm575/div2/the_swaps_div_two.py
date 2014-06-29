class TheSwapsDivTwo:
    def find(self, sequence):
        l, s = len(sequence), set()
        for i in xrange(l):
            for j in xrange(i+1, l):
                s.add(tuple(
                            sequence[:i] +
                            (sequence[j],) +
                            sequence[i+1:j] +
                            (sequence[i],) +
                            sequence[j+1:]))
        return len(s)
