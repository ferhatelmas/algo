import sys


def get_direction(o, p, r, q):
    if o == r and p == q:
        return 'here'
    elif p < q:
        if o < r:
            return 'NE'
        elif o > r:
            return 'NW'
        else:
            return 'N'
    elif p == q:
        if o < r:
            return 'E'
        else:
            return 'W'
    elif p > q:
        if o < r:
            return 'SE'
        elif o > r:
            return 'SW'
        else:
            return 'S'


with open(sys.argv[1], 'rb') as test_cases:
    for test in test_cases:
        print get_direction(*map(int, test.split()))
