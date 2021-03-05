from itertools import groupby


class LittleElephantAndBallsAgain:
    def getNumber(self, S):
        m = max(len(list(g)) for k, g in groupby(S))
        return len(S) - m
