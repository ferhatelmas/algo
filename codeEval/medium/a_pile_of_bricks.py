import sys


def strip_split(x):
    return map(int, x.strip("[]").split(","))


def diff(x):
    return abs(x[0] - x[1])


def is_possible(h, b):
    return h[0] >= b[0] and h[1] >= b[1]


def dim(*args):
    return sorted(map(diff, zip(*map(strip_split, args))))


def can_pass_through(hole, piles):
    return ",".join(
        map(str, sorted(int(i) for i, x, y in piles if is_possible(hole, dim(x, y))))
    )


test_cases = open(sys.argv[1], "r")
for test in test_cases:
    hole, piles = test.strip().split("|")
    r = can_pass_through(
        sorted(map(diff, zip(*map(strip_split, hole.split())))),
        map(lambda e: e.strip("()").split(), piles.split(";")),
    )
    print r if r else "-"
test_cases.close()
