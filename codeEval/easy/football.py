import sys
from collections import defaultdict


def teams(ls):
    d = defaultdict(list)
    for i, l in enumerate(ls, start=1):
        s = str(i)
        for n in map(int, l.split()):
            d[n].append(s)
    return " ".join("{}:{};".format(k, ",".join(d[k])) for k in sorted(d.keys()))


with open(sys.argv[1], "r") as test_cases:
    for test in test_cases:
        print(teams(test.rstrip().split("|")))
