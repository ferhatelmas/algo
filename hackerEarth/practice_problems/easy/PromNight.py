from sys import stdin

for i, ln in enumerate(stdin, start=-1):
    if i == -1:
        continue
    c = i % 3
    if c == 0:
        n, m = map(int, ln.split())
    elif c == 1:
        a = map(int, ln.split())
    else:
        b = map(int, ln.split())
        print("NO", "YES")[all(x > y for x, y in zip(sorted(a), sorted(b)))]
