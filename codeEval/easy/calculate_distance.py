import sys

test_cases = open(sys.argv[1], "r")
for test in test_cases:
    p1, p2 = map(lambda e: map(int, e.split(",")), test.strip()[1:-1].split(") ("))
    print int((abs(p1[0] - p2[0]) ** 2 + abs(p1[1] - p2[1]) ** 2) ** 0.5)
test_cases.close()
