from operator import mul

for _ in xrange(int(raw_input())):
    print reduce(mul, xrange(1, int(raw_input()) + 1))
