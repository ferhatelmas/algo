import sys


primes = [3, 7, 31, 127, 2047]


with open(sys.argv[1], "r") as test_cases:
    for test in test_cases:
        n = int(test)
        print(", ".join(str(e) for e in primes if e < n))
