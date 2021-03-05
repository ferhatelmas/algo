import sys


def make(ls):
    n = int(len(ls) ** 0.5)
    return [ls[i * n : (i + 1) * n] for i in xrange(n)]


def rotate(ls):
    return " ".join(" ".join(reversed(r)) for r in zip(*ls))


with open(sys.argv[1], "r") as test_cases:
    for test in test_cases:
        print rotate(make(test.rstrip().split(" ")))
