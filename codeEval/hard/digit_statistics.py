import sys


def get_statistics(a, n):
    ls, r = [], a
    while r not in ls:
        ls.append(r)
        r = (r * a) % 10

    x, y = divmod(n, len(ls))
    c = {e: x + int(i < y) for i, e in enumerate(ls)}
    return ', '.join('{}: {}'.format(i, c.get(i, 0)) for i in xrange(10))


with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        print get_statistics(*map(int, test.split()))
