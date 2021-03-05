import sys

test_cases = open(sys.argv[1], "r")
for test in test_cases:
    s, rm = test.split(", ")
    print filter(lambda x: not (x in rm), s).strip()
test_cases.close()
