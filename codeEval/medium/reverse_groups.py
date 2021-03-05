import sys


def reverse_groups(ls, k):
    res = []
    for i in xrange(len(ls) // k):
        l = ls[i * k : (i + 1) * k]
        l.reverse()
        res.append(l)
    res.append(ls[(len(ls) // k) * k :])
    return ",".join([x for l in res for x in l])


test_cases = open(sys.argv[1], "r")
for test in test_cases:
    ls, k = test.split(";")
    print reverse_groups(ls.split(","), int(k))
test_cases.close()
