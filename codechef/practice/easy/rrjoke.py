from operator import xor
from sys import stdin


n = 0
for i, ln in enumerate(stdin):
    if not i:
        continue
    if not n:
        n = int(ln)
        print reduce(xor, xrange(1, n + 1), 0)
    else:
        n -= 1
