import sys, itertools


def perm(s):
    return ",".join(sorted(["".join(x) for x in itertools.permutations(s)]))


test_cases = open(sys.argv[1], "r")
for test in test_cases:
    print perm(test.strip())
test_cases.close()
