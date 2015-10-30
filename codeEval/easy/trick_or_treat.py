import sys


with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        p = [int(e.split(':')[1]) for e in test.split(',')]
        s = sum(p[3] * c * i for c, i in zip(p[:-1], (3, 4, 5)))
        print(s // sum(p[:-1]))
