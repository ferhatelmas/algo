for _ in xrange(int(raw_input())):
    raw_input()
    d = {}
    mc, mi = 0, None
    for e in raw_input().split():
        if e in d:
            d[e] += 1
        else:
            d[e] = 1

        if d[e] > mc or (d[e] == mc and int(e) < int(mi)):
            mc = d[e]
            mi = e

    print "%s %d" % (mi, mc)
