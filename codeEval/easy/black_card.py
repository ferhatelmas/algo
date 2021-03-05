import sys


def solve(ls, n):
    c = len(ls)
    while c > 1:
        i, c = n % c - 1, c - 1
        ls = ls[:i] + ls[i + 1 :]
    return ls[0]


with open(sys.argv[1], "r") as test_cases:
    for test in test_cases:
        ls, n = test.split("|")
        print(solve(ls.split(), int(n)))
