import sys


def is_ugly(n):
    return any(n % m == 0 for m in [2, 3, 5, 7])


def count(ls):
    l = len(ls)
    d = [[0] * 210 for _ in xrange(l + 1)]
    d[0][0] = 1

    for i in xrange(l):
        for s in range(1 if i == 0 else -1, 2, 2):
            v = 0
            for j in xrange(i, l):
                v = (v * 10 + int(ls[j])) % 210
                for k in xrange(210):
                    d[j + 1][(k + s * v) % 210] += d[i][k]
    return sum(map(lambda i: d[l][i], filter(is_ugly, xrange(210))))


test_cases = open(sys.argv[1], "r")
for test in test_cases:
    print count(test.strip())
test_cases.close()
