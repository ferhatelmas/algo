import sys

mapping = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]
d = dict(zip(mapping, xrange(10)))


def get_number(ns):
    return "".join(map(lambda n: str(d[n]), ns))


test_cases = open(sys.argv[1], "r")
for test in test_cases:
    print get_number(test.strip().split(";"))
test_cases.close()
