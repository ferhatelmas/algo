from sys import stdin


for i, ln in enumerate(stdin):
    if i:
        n, k = map(int, ln.split())
        if k:
            print '{} {}'.format(*divmod(n, k))
        else:
            print 0, n
