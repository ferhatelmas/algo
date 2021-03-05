import re, sys


def is_inside(c, r, p):
    if r[0] >= ((c[0] - p[0]) ** 2 + (c[1] - p[1]) ** 2) ** 0.5:
        return "true"
    return "false"


def to_tuple(s):
    return tuple(float(d) for d in re.findall("[0-9\.\-]+", s))


test_cases = open(sys.argv[1], "r")
for test in test_cases:
    c, r, p = map(lambda e: to_tuple(e.split(":")[1]), test.strip().split(";"))
    print is_inside(c, r, p)
test_cases.close()
