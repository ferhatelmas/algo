import sys


def update_row(res, ls):
    return [max(x, y) + z for (x, y, z) in zip([0] + res, res + [0], ls)]


res = []
test_cases = open(sys.argv[1], "r")
for test in test_cases:
    res = update_row(res, map(int, test.strip().split()))
test_cases.close()

print max(res)
