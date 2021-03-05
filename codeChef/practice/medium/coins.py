from sys import stdin, stdout

cache = {}


def getMax(n):
    if n in cache:
        return cache[n]
    if n == 0:
        return 0

    cache[n] = max(n, getMax(n / 2) + getMax(n / 3) + getMax(n / 4))
    return cache[n]


stdout.write("\n".join(map(str, map(getMax, map(int, stdin.readlines())))))
