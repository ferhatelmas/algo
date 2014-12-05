import sys
from itertools import groupby


with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        print ''.join(k for k, _ in groupby(test.rstrip()))
