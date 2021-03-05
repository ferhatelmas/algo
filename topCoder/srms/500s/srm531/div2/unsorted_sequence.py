class UnsortedSequence:
    def getUnsorted(self, s):
        if len(set(s)) < 2:
            return []
        s = sorted(s)
        x = s[-1]
        i = s.count(x)
        s[-i - 1], s[-i] = s[-i], s[-i - 1]
        return s
