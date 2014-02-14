import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    n, p = test.split()
    for i, e in enumerate(p):
        if e in '-+':
            a, b = int(n[:i]), int(n[i:])
            print a+b if e == '+' else a-b
            break
test_cases.close()
