from operator import itemgetter

class LoveCalculator:
    def findBoy(self, girl, boys):
        g = [girl.count(e) for e in 'LOVE']
        def prob(boy):
            l, o, v, e = [boy.count(e) + g[i] for i, e in enumerate('LOVE')]
            return ((l+o) * (l+v) * (l+e) * (o+v) * (o+e) * (v+e)) % 100
        ls = [(b, -prob(b)) for b in boys]
        return sorted(ls, key=itemgetter(1, 0))[0][0]
