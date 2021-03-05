import sys


def step(ls, r):
    l, i = len(ls), 0
    while i < r:
        curr, is_sorted = -1, True
        for j in xrange(1, l):
            if ls[j - 1] > ls[j]:
                ls[j - 1], ls[j] = ls[j], ls[j - 1]
                curr, is_sorted = j, False
        if is_sorted:
            break
        l = curr
        i += 1
    return ls


test_cases = open(sys.argv[1], "r")
for test in test_cases:
    ns, k = test.rstrip().split("|")
    print " ".join(str(e) for e in step(map(int, ns.split()), int(k)))
test_cases.close()
