from operator import itemgetter


class CustomerStatistics:
    def reportDuplicates(self, customerNames):
        d = {}
        for n in customerNames:
            d[n] = d.get(n, 0) + 1
        return map(
            lambda (k, v): "{} {}".format(k, v),
            sorted(filter(lambda (k, v): v > 1, d.items()), key=itemgetter(0)),
        )
