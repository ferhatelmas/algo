import sys
from operator import itemgetter


def do_segment(s, n, d):
    sl, ls = len(s), []
    for i in xrange(len(d) - sl):
        curr, b, f = range(1, sl + 1) + [0], d[i : i + sl], True
        for x in xrange(sl):
            prev, curr = curr, [0] * sl + [x + 1]
            for y in xrange(sl):
                curr[y] = min(
                    prev[y] + 1, curr[y - 1] + 1, prev[y - 1] + (s[x] != b[y])
                )
            if min(curr) > n:
                f = False
                break
        if f and curr[sl - 1] <= n:
            ls.append((b, curr[sl - 1]))
    return (
        " ".join(e for e, _ in sorted(ls, key=itemgetter(1, 0))) if ls else "No match"
    )


test_cases = open(sys.argv[1], "r")
for test in test_cases:
    s, n, d = test.split()
    print do_segment(s, int(n), d)
test_cases.close()
