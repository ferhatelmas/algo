import sys


def get_major(ls):
    i, c = 0, 1
    for j, e in enumerate(ls):
        c += 1 if ls[i] == e else -1
        if c == 0:
            i, c = j, 1
    if ls.count(ls[i]) > j / 2:
        return ls[i]


test_cases = open(sys.argv[1], "r")
for test in test_cases:
    print get_major(test.rstrip().split(","))
test_cases.close()
