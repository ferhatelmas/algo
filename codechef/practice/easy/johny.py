from sys import stdin


for i, ln in enumerate(stdin):
    if i > 0:
        if i % 3 == 2:
            ls = map(int, ln.split())
        elif i % 3 == 0:
            k = ls[int(ln) - 1]
            print sorted(ls).index(k) + 1
