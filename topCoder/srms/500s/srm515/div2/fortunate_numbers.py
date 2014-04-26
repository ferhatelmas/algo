from itertools import product

class FortunateNumbers:
    def getFortunate(self, a, b, c):
        s, f = set(), set(['5', '8'])
        for i, j, k in product(a, b, c):
            n = i+j+k
            if n not in s and not (set(str(n)) - f):
                s.add(n)
        return len(s)
