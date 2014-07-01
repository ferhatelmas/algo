class LeftAndRightHandedDiv2:
    def count(self, S):
        return sum(i == 'R' and j == 'L' for i, j in zip(S, S[1:]))
