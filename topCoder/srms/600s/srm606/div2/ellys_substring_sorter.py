class EllysSubstringSorter:
    def getMin(self, S, L):
        m = "Z" * len(S)
        for i in xrange(len(S) - L + 1):
            s = S[:i] + "".join(sorted(S[i : i + L])) + S[i + L :]
            m = min(m, s)
        return m
