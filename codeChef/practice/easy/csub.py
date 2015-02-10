from sys import stdin


for i, ln in enumerate(stdin):
    if i and i % 2 == 0:
        n = ln.count('1')
        print(n * (n + 1) / 2)
