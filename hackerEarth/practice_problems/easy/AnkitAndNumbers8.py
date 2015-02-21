from itertools import combinations


def cnt1(n):
    return sum(
        sum(j)
        for i in xrange(1, n + 1)
        for j in combinations(range(1, n + 1), i)
    )


def cnt2(n):
    return n * (n + 1) * 2 ** (n - 2)


def test():
    for n in xrange(1, 20):
        assert cnt1(n) == cnt2(n)

test()
