import sys
from collections import defaultdict


def tree():
    return defaultdict(tree)


def hierarchy(d, keys):
    return ", ".join(
        "{} [{}]".format(e, hierarchy(d, sorted(d[e].keys())))
        if d[e]
        else "{}".format(e)
        for e in keys
    )


with open(sys.argv[1], "r") as test_cases:
    for test in test_cases:
        d, h = tree(), None
        for e in test.split("|"):
            a, b = e.strip()
            d[a][b]
            if h is None:
                h = a
        print(hierarchy(d, [h]))
