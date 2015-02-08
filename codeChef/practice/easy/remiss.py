from sys import stdin


for i, ln in enumerate(stdin):
    if i:
        a, b = map(int, ln.split())
        print max(a, b), a + b
