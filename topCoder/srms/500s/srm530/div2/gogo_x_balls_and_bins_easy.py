class GogoXBallsAndBinsEasy:
    def solve(self, T):
        return sum(abs(j-i)
                   for i, j in zip(sorted(T), sorted(T, reverse=True)))/2
