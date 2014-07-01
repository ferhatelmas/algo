from itertools import groupby

class AlienAndPassword:
    def getNumber(self, S):
        return sum(1 for _ in groupby(S))
