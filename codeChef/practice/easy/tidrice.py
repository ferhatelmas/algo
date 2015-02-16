from sys import stdin

n = 0
for i, ln in enumerate(stdin):
    if i:
        if not n:
            n, d = int(ln), {}
        else:
            name, vote = ln.split()
            d[name] = 1 if vote == '+' else -1
            n -= 1
            if not n:
                print sum(d.values())
