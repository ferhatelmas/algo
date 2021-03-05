for _ in xrange(int(raw_input())):
    n = int(raw_input())

    m = n
    for a in xrange(1, int(n ** 0.5 + 1)):
        if n % a == 0:
            b = n / a
            m = min(m, abs(a - b))

    print m
