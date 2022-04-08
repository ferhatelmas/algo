for _ in range(int(input())):
    input()
    d = {}
    mc, mi = 0, None
    for e in input().split():
        if e in d:
            d[e] += 1
        else:
            d[e] = 1

        if d[e] > mc or (d[e] == mc and int(e) < int(mi)):
            mc = d[e]
            mi = e

    print("%s %d" % (mi, mc))
