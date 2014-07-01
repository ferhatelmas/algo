class MagicalStringDiv2:
    def minimalMoves(self, S):
        l = len(S)
        return sum(S[i] == ('<' if i<l/2 else '>') for i in xrange(l))
