import sys


cache = {}
coins = (1, 5, 10, 25, 50)


def solve(t, k):
    if t < 0 or k <= 0:
        return 0
    if t == 0:
        return 1
    i = 5 * t + k
    if i in cache:
        return cache[i]
    cache[i] = solve(t, k - 1) + solve(t - coins[k - 1], k)
    return cache[i]


with open(sys.argv[1], "r") as test_cases:
    for test in test_cases:
        print(solve(int(test), 5))
