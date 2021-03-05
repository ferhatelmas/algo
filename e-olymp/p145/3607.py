from collections import Counter
from sys import stdin


for i, ln in enumerate(stdin):
    c = i % 3
    if c == 1:
        cnt = Counter(ln.rstrip().split())
    elif c == 2:
        a, b = ln.rstrip().split()
        print(sum(cnt[str(i)] for i in range(int(a), int(b) + 1)))
