import sys


def josephus(n, k):
    a, f, i, l = range(n), [], 0, n
    while l > 0:
        j = k
        while j > 1:
            i = (i + 1) % l
            j -= 1
        f.append(a.pop(i))
        l -= 1
    return " ".join(map(str, f))


test_cases = open(sys.argv[1], "r")
for test in test_cases:
    n, k = map(int, test.split(","))
    print josephus(n, k)
test_cases.close()
