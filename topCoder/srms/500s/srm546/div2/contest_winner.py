from collections import OrderedDict
from operator import itemgetter


class ContestWinner:
    def getWinner(self, events):
        d = OrderedDict()
        for i, e in enumerate(events):
            if e in d:
                d[e] = (d[e][0] + 1, -i)
            else:
                d[e] = (1, -i)
        return max(d.items(), key=itemgetter(1))[0]
