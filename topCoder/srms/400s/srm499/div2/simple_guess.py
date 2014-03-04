class SimpleGuess:
    def getMaximum(self, hints):
        def p(m, n):
            c = m + n
            if c%2 == 0:
                c /= 2
                return (max(m, n) - c) * c
            return 0
        return max(p(m, n)
                   for i, m in enumerate(hints)
                   for n in hints[i:])
