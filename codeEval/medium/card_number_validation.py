import sys


def is_valid(s):
    return (
        sum(
            sum(map(int, str(int(e) * (1 + i % 2))))
            for i, e in enumerate(reversed(s.replace(" ", "")))
        )
        % 10
        == 0
    )


with open(sys.argv[1], "r") as test_cases:
    for test in test_cases:
        print int(is_valid(test.rstrip()))
