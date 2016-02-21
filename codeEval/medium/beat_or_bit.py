import sys


def convert(n):
    for i, e in enumerate(n):
        if i == 0:
            r = e
        else:
            r += ("1", "0")[e == r[-1]]
    return str(int(r, 2))


def solve(ls):
    return " | ".join(convert(e) for e in ls)


with open(sys.argv[1], "r") as test_cases:
    for test in test_cases:
        print(solve(e.strip() for e in test.split("|")))
