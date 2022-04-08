for _ in xrange(int(raw_input())):
    n, m = raw_input().split()
    f = map(int, raw_input().split())
    f.sort()

    fi = range(1, int(n) + 1)
    for i in f:
        fi.remove(i)

    l = len(fi)
    print " ".join(map(str, [fi[i] for i in xrange(0, l, 2)]))
    print " ".join(map(str, [fi[i] for i in xrange(1, l, 2)]))
