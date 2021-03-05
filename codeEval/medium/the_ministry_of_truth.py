import re
import sys


def r(s):
    return "_" * len(s)


def c(*a):
    ls, lu = [re.split("\s+", e) for e in a]
    i, j, li, lj = 0, 0, len(ls), len(lu)
    res = []
    while i < li and j < lj:
        k = ls[i].find(lu[j])
        if k != -1:
            res.append("_" * k + lu[j] + "_" * (len(ls[i]) - len(lu[j]) - k))
            j += 1
        else:
            res.append(r(ls[i]))
        i += 1

    res.extend(r(s) for s in ls[i:])

    if j == lj:
        return " ".join(res)
    return "I cannot fix history"


test_cases = open(sys.argv[1], "r")
for test in test_cases:
    print c(*test.rstrip().split(";"))
test_cases.close()
