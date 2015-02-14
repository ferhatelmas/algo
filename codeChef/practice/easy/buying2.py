from sys import stdin


for i, ln in enumerate(stdin):
    if i:
        if i % 2 == 0:
            _, n = map(int, ln.split())
        else:
            ls = map(int, ln.split())
            i, j = divmod(sum(ls), n)
            print -1 if j >= min(ls) else i
