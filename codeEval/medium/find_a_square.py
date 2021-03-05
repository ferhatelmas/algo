import sys, itertools


def dist(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5


def is_equi_distant(ps):
    l = len(ps)
    ds = [dist(ps[i % l], ps[(i + 1) % l]) for i in xrange(l)]
    return (
        all(d == ds[0] for d in ds)
        and abs(dist(ps[0], ps[2]) - 2 ** 0.5 * ds[0]) < 0.00001
    )


def is_square(ps):
    for p in itertools.permutations(ps[1:]):
        if is_equi_distant((ps[0],) + p):
            return "true"
    return "false"


test_cases = open(sys.argv[1], "r")
for test in test_cases:
    print is_square(list(eval(test)))
test_cases.close()
