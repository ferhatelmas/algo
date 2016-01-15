import sys


def step(ls, l):
    for i in xrange(0, l-1):
        if ls[i] > ls[i+1]:
            ls[i+1], ls[i] = ls[i], ls[i+1]
    for i in xrange(l-1, 0, -1):
        if ls[i] < ls[i-1]:
            ls[i], ls[i-1] = ls[i-1], ls[i]


def cocktail(ls, n):
    l = len(ls)
    while n > 0:
        n -= 1
        step(ls, l)
    return " ".join(map(str, ls))


with open(sys.argv[1], "r") as test_cases:
    for test in test_cases:
        a, b = test.split("|")
        print(cocktail(map(int, a.split()), int(b)))
