from sys import stdin


for i, ln in enumerate(stdin):
    if i:
        if i % 2 == 1:
            s = set(ln.rstrip())
        else:
            print(sum(e in s for e in ln.rstrip()))
