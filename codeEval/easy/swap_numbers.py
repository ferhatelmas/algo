from sys import argv


with open(argv[1], "r") as test_cases:
    for test in test_cases:
        print(" ".join(e[-1] + e[1:-1] + e[0] for e in test.split()))
