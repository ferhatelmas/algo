import sys


vals = "00234567891JQKA"


def rank(c, t):
    v = vals.index(c[0])
    if c[-1] == t:
        v <<= 4
    return v


def win(cs, t):
    a, b = [rank(c, t) for c in cs]
    if a > b:
        return cs[0]
    elif a < b:
        return cs[1]
    return "{} {}".format(*cs)


with open(sys.argv[1], "r") as test_cases:
    for test in test_cases:
        cs, t = test.rstrip().split("|")
        print(win(cs.split(), t.strip()))
