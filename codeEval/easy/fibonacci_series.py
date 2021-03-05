import sys


def fib(f, l, n):
    while l < n:
        f.append(f[-2] + f[-1])
        l += 1
    return f, l, f[n]


l = 1
f = [0, 1]

test_cases = open(sys.argv[1], "r")
for test in test_cases:
    f, l, test = fib(f, l, int(test))
    print test
test_cases.close()
