from itertools import groupby
from operator import itemgetter

class ClassScores:
    def findMode(self, scores):
        r = sorted(map(lambda (k, g): (k, len(list(g))), groupby(sorted(scores))),
                   key=itemgetter(1), reverse=True)
        return [i for i, n in r if n == r[0][1]]
