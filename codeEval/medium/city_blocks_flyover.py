import sys


def fly(xs, ys):
    r = ys[-1] / float(xs[-1])
    def contains(a, b, c, d):
        return not(r * a >= d or r * b <= c)
    return sum(contains(x1, x2, y1, y2) for x1, x2 in zip(xs, xs[1:]) for y1, y2 in zip(ys, ys[1:]))


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    xs, ys = [map(int, e.strip('()').split(',')) for e in test.split()]
    print fly(xs, ys)
test_cases.close()
