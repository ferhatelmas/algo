import sys


with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        t = [map(int, e.split()) for e in test.rstrip().split('|')]
        print(' '.join(str(max(e)) for e in zip(*t)))
