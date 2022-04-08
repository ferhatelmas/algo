from sys import maxint, stdin


for i, ln in enumerate(stdin):
    if i > 0 and i % 2 == 0:
        m, c = maxint, 0
        for e in map(int, ln.split()):
            if e <= m:
                c += 1
                m = e
        print c
