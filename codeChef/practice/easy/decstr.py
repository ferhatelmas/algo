for _ in xrange(int(raw_input())):
    n = int(raw_input())
    r = map(chr, (range(97, 123) * (n / 25)))
    if n % 25 > 0:
        r += map(chr, range(97, 98 + n % 25))
    r.reverse()
    print "".join(r)
