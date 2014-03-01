import sys


def fly(xs, ys):
    r = ys[-1] / float(xs[-1])
    return sum(not(r * x1 >= y2 or r * x2 <= y1)
               for x1, x2 in zip(xs, xs[1:])
               for y1, y2 in zip(ys, ys[1:]))


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    print fly(*[map(int, e.strip('()').split(',')) for e in test.split()])
test_cases.close()
