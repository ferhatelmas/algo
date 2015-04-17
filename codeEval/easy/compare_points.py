import sys


def get_direction(o, p, r, q):
    a, b = 'hSN'[cmp(p, q)], 'hWE'[cmp(o, r)]
    if a == b:
        return 'here'
    return (a + b).replace('h', '')


with open(sys.argv[1], 'rb') as test_cases:
    for test in test_cases:
        print get_direction(*map(int, test.split()))
