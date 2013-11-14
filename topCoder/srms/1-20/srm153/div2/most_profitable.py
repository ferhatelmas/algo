from operator import itemgetter

class MostProfitable:
    def bestItem(self, costs, prices, sales, items):
        res = sorted(map(lambda (c, p, s, i, j): ((p-c)*s, i, j),
                         zip(costs, prices, sales, items, range(len(items), -1, -1))),
                     key=itemgetter(0, 2))
        if res and res[-1][0] > 0:
            return res[-1][1]
        return ""
