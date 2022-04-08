from sys import stdin
from itertools import groupby

for i, ln in enumerate(stdin):
    if i > 0 and i % 2 == 0:
        s = "0" + ln.rstrip() + "0"
        print(sum(max(len(list(g)) - 2, 0) for k, g in groupby(s) if k == "0"))
