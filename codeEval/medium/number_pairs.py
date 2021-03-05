import sys


def pairs(ls, n):
    l, p, cnt = len(ls), [], 0
    for i in xrange(l):
        for j in xrange(i + 1, l):
            s = ls[i] + ls[j]
            if s == n:
                p.append(str(ls[i]) + "," + str(ls[j]))
                cnt += 1
            elif s > n:
                break
    if cnt == 0:
        print "NULL"
    else:
        print ";".join(p)


test_cases = open(sys.argv[1], "r")
for test in test_cases:
    l, n = test.split(";")
    pairs(map(int, l.split(",")), int(n))
test_cases.close()
