from sys import stdin

p1, p2 = 0, 1
cache = {0, 1}


def is_fib(n):
    global p1, p2
    while p2 < n:
        p1, p2 = p2, p1 + p2
        cache.add(p2)
    return n in cache


print "\n".join(("NO", "YES")[is_fib(int(e))] for i, e in enumerate(stdin) if i)
