import calendar
import sys

months = dict(zip(calendar.month_abbr[1:], range(12)))


def get_experience(ls):
    f = [[False] * 12 for _ in xrange(31)]
    for p in ls:
        s, e = [i.split() for i in p.split("-")]
        i, j = months[s[0]], int(s[1]) - 1990
        k, l = months[e[0]], int(e[1]) - 1990
        while j < l or (j == l and i <= k):
            f[j][i] = True
            if i == 11:
                j += 1
                i = 0
            else:
                i += 1
    return sum(sum(r) for r in f) / 12


test_cases = open(sys.argv[1], "r")
for test in test_cases:
    print get_experience(test.split(";"))
test_cases.close()
