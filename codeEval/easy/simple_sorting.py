import sys

test_cases = open(sys.argv[1], "r")
for test in test_cases:
    print " ".join(
        map(lambda f: "%.3f" % (f,), sorted(map(float, test.strip().split())))
    )
test_cases.close()
