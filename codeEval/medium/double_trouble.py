import sys


def cases(s):
    c = 0
    for a, b in zip(s, s[len(s) // 2 :]):
        if a == b == "*":
            c += 1
        elif a != b and not (a == "*" or b == "*"):
            return 0
    return 2 ** c


with open(sys.argv[1], "r") as test_cases:
    for test in test_cases:
        print(cases(test.rstrip()))
