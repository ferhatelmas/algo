from operator import itemgetter

class MostProfitable:
    def bestItem(self, costs, prices, sales, items):
        ls = filter(lambda (c, i): c > 0,
            map(lambda (c, p, s, i): ((p-c)*s, i), zip(costs, prices, sales, items))
        )
        return max(ls, key=itemgetter(0))[1] if ls else ''
