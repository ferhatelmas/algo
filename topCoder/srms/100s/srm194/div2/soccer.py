class Soccer:
    def maxPoints(self, wins, ties):
        return max(map(lambda (w, t): 3*w + t, zip(wins, ties)))
