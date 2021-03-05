class SemiPerfectSquare:
    def check(self, N):
        l, u = int(N ** 0.33), int(N ** 0.5)
        for b in xrange(l, u + 1):
            for a in xrange(1, b):
                if a * b * b == N:
                    return "Yes"
        return "No"
