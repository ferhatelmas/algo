from operator import itemgetter

class Barbecue:
    def eliminate(self, n, voter, excluded):
        ls = [(n-i, voter.count(i), excluded.count(i)) for i in xrange(n)]
        ls.sort(key=itemgetter(2, 1, 0), reverse=True)
        return n-ls[0][0]
