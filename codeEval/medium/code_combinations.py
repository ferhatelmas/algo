import sys


def order(ls, i, j):
    c = "".join(sorted(e for l in ls[i : i + 2] for e in l[j : j + 2]))
    return c


def count(ls):
    return sum(
        "cdeo" == order(ls, i, j)
        for i in range(len(ls) - 1)
        for j in range(len(ls[0]) - 1)
    )


with open(sys.argv[1], "r") as test_cases:
    for test in test_cases:
        m = [list(e.strip()) for e in test.rstrip().split("|")]
        print(count(m))
