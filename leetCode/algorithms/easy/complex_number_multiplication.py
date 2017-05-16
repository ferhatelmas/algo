class Solution(object):
    def complexNumberMultiply(self, a, b):
        def r(x):
            return [int(e.rstrip('i')) for e in x.split('+')]

        a1, b1 = r(a)
        a2, b2 = r(b)
        return '{}+{}i'.format(a1 * a2 - b1 * b2, a1 * b2 + a2 * b1)
