from sys import argv


def get_arrow_count(s):
    return sum(s[i : i + 5] in (">>-->", "<--<<") for i in xrange(len(s) - 4))


with open(argv[1], "r") as test_cases:
    for test in test_cases:
        print(get_arrow_count(test.rstrip()))
