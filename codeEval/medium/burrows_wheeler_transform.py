import sys


def inverse(s):
    l = len(s)
    ls = ['' for _ in xrange(l)]
    for _ in xrange(l):
        ls = sorted(a + b for a, b in zip(s, ls))
    for t in ls:
        if t[-1] == '$':
            return t


with open(sys.argv[1], 'rb') as f:
    for ln in f:
        print inverse(ln.rstrip()[:-1])
