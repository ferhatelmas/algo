import sys


with open(sys.argv[1], "r") as test_cases:
    for test in test_cases:
        k, n = map(int, test.split())
        print(sum(bin(i)[2:].count("0") == k for i in range(1, n + 1)))
