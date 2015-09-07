import re
import sys


def walk(m, n, x, y):
    c = 0
    while n > y:
        c, m, n, x, y = c + m, n - 1, m, n - y, x
    return c + x


with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        print(walk(*map(int, re.findall(r'\d+', test))))
