from operator import itemgetter

class CarrotBoxesEasy:
    def theIndex(self, carrots, K):
        c = list(carrots)
        def eat(cs):
            i, m = max(enumerate(cs), key=itemgetter(1))
            cs[i] -= 1
            return i
        while K:
            i = eat(c)
            K -= 1
        return i
