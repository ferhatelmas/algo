from sys import stdin
from itertools import groupby

for i, s in enumerate(stdin):
    if i:
        print(
            sum(
                (l / 2) + (l % 2)
                for l in (len(list(g)) for k, g in groupby(sorted(s.rstrip())))
            )
        )
