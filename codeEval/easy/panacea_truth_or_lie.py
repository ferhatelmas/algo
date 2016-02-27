import sys


def sums(ls, base):
    return sum(int(e, base) for e in ls.split())


with open(sys.argv[1], "r") as test_cases:
    for test in test_cases:
        virus, anti = test.split("|")
        print(sums(virus, 16) <= sums(anti, 2))
