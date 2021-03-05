import sys


def get_ratio(s):
    n, sl = sum("a" <= e <= "z" for e in s), float(len(s))
    return "lowercase: %.2f uppercase: %.2f" % (n * 100 / sl, (sl - n) * 100 / sl)


test_cases = open(sys.argv[1], "r")
for test in test_cases:
    print get_ratio(test.rstrip())
test_cases.close()
