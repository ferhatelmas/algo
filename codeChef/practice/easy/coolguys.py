from fractions import gcd
from sys import stdin


def p(n):
    s = int(n ** 0.5)
    c = sum(n / i for i in xrange(1, s + 1)) * 2 - s ** 2
    g = gcd(c, n ** 2)
    return "{}/{}".format(c / g, n ** 2 / g)


print("\n".join(p(int(ln)) for i, ln in enumerate(stdin) if i))
