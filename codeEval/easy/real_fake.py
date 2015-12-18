import sys


def point(s):
    return sum(2 * int(e) if i % 2 == 0 else int(e) for i, e in enumerate(s))


def is_valid(ls):
    return sum(point(l) for l in ls) % 10 == 0


with open(sys.argv[1], "r") as test_cases:
    for test in test_cases:
        print(("Fake", "Real")[is_valid(test.rstrip().split())])
