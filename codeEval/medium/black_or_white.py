import sys


def count(ls, l, r, c):
    return sum(ls[i][c : c + l].count("1") for i in range(r, r + l))


def solve(ls):
    l = len(ls)
    for i in range(1, l + 1):
        c, n = set(), 0
        for j in range(l - i + 1):
            for k in range(l - i + 1):
                n += 1
                c.add(count(ls, i, j, k))
        if len(c) == 1:
            return "{0}x{0}, {1}".format(i, c.pop())


with open(sys.argv[1], "r") as test_cases:
    for test in test_cases:
        ls = [list(e.strip()) for e in test.split("|")]
        print(solve(ls))
