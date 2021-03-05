import sys

test_cases = open(sys.argv[1], "r")
for test in test_cases:
    n, p1, p2 = map(int, test.strip().split(","))
    n = list(bin(n))
    n.reverse()
    if n[p1 - 1] == n[p2 - 1]:
        print "true"
    else:
        print "false"
test_cases.close()
