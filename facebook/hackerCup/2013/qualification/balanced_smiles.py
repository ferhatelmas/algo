import sys


def valid(s, cnt):
    l = len(s)
    for i in xrange(l):
        if s[i] in "()":
            return (
                (s[i] == "(" and valid(s[i + 1 :], cnt + 1))
                or (s[i] == ")" and cnt > 0 and valid(s[i + 1 :], cnt - 1))
                or (i > 0 and s[i - 1] == ":" and valid(s[i + 1 :], cnt))
            )
    return cnt == 0


def is_valid(s):
    return "YES" if valid(s, 0) else "NO"


i, f = 0, open(sys.argv[1], "r")
for l in f:
    if i > 0:
        print "Case #%d: %s" % (i, is_valid(l.strip()))
    i += 1
f.close()
