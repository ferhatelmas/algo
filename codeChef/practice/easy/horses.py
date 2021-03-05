from sys import stdin


for i, ln in enumerate(stdin):
    if i > 0 and i % 2 == 0:
        ls = sorted(map(int, ln.split()))
        print min(b - a for a, b in zip(ls, ls[1:]))
