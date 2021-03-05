import sys


def step():
    global flags, ls

    def count(i, j):
        return sum(
            ls[i + n][max(0, j - 1) : j + 2].count("*")
            for n in xrange(-1, 2)
            if 0 <= i + n < l
        )

    for i, r in enumerate(ls):
        for j, c in enumerate(r):
            e = count(i, j)
            if c == "*":
                flags[i][j] = 2 <= (e - 1) <= 3
            else:
                flags[i][j] = e == 3

    for i, r in enumerate(flags):
        for j, c in enumerate(r):
            ls[i][j] = "*" if c else "."


test_cases = open(sys.argv[1], "r")
ls = [list(test.rstrip()) for test in test_cases]
test_cases.close()
l = len(ls)
flags = [[False] * l for _ in xrange(l)]
for _ in xrange(10):
    step()
for r in ls:
    print "".join(r)
