from itertools import izip

class CandyShop:
    def countProbablePlaces(self, X, Y, R):
        def generate(x, y, r):
            s = set()
            for i in xrange(r+1):
                for j in xrange(r-i+1):
                    s.add((x+i, y+j))
                    s.add((x-i, y+j))
                    s.add((x+i, y-j))
                    s.add((x-i, y-j))
            return s
        return len(reduce(lambda a, b: a&b, (generate(*e) for e in izip(X, Y, R))))
