from sys import argv


def stepwise(s):
    return " ".join("*" * i + e for i, e in enumerate(s))


with open(argv[1], "r") as test_cases:
    for test in test_cases:
        print(stepwise(max(test.rstrip().split(), key=len)))
