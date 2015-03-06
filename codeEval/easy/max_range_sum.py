import sys


with open(sys.argv[1], 'rb') as test_cases:
    for test in test_cases:
        n, ls = test.split(';')
        n, ls = int(n), map(int, ls.split())
        m = s = sum(ls[:n])

        for i, e in enumerate(ls[n:], n):
            s += (e - ls[i - n])
            m = max(m, s)
        print(max(m, 0))
