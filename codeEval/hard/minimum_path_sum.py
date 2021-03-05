import sys


def get_min_path_sum(m, n):
    for i in xrange(n):
        for j in xrange(n):
            r = min(
                m[i - 1][j] if i > 0 else sys.maxint,
                m[i][j - 1] if j > 0 else sys.maxint,
            )
            m[i][j] += r if r != sys.maxint else 0
    return m[n - 1][n - 1]


test_cases = open(sys.argv[1], "r")
while True:
    s = test_cases.readline()
    if s == "":
        break
    print get_min_path_sum(
        [map(int, test_cases.readline().split(",")) for _ in xrange(int(s))], int(s)
    )
test_cases.close()
