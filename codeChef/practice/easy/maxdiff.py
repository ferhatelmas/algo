from sys import stdin


for i, ln in enumerate(stdin):
    if i:
        if i % 2:
            _, k = map(int, ln.split())
        else:
            ls = sorted(map(int, ln.split()))
            print max(
                abs(sum(ls[k:]) - sum(ls[:k])),
                abs(sum(ls[:-k]) - sum(ls[-k:]))
            )
