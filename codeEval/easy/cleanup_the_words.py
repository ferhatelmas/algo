import re
import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        ls = re.split(r'[^a-zA-Z]', test.rstrip())
        print(' '.join(e.lower() for e in ls if e))
