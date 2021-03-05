from math import sqrt

for _ in xrange(int(raw_input())):
    p, s = map(int, raw_input().split())
    a = (p - sqrt(p ** 2 - 24 * s)) / 12
    print "%.2f" % ((p / 4.0 - 2 * a) * a ** 2)
