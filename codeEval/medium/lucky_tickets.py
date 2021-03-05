from math import factorial as f
from math import floor as low
from sys import argv


def nCk(n, k):
    return f(n) / (f(k) * f(n - k))


def solve(n):
    return sum(
        (-1) ** k * nCk(n, k) * nCk(n + low(9 * n / 2) - 10 * k - 1, n - 1)
        for k in range(int(low((9 * n / 20) + 1)))
    )


with open(argv[1], "r") as test_cases:
    for test in test_cases:
        print(solve(int(test)))
