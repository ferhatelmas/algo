from sys import stdin

q, c = 0, -1
for i, ln in enumerate(stdin):
    if i:
        if q:
            l, r = map(int, ln.split())
            if l <= c <= r:
                c = r - (c - l)
            q -= 1
            if q == 0:
                print(c)
        else:
            n, c, q = map(int, ln.split())
