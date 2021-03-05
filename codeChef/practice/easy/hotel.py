for _ in xrange(int(raw_input())):
    n = int(raw_input())
    a = sorted(map(int, raw_input().split()))
    d = sorted(map(int, raw_input().split()))

    i, j, m, mi = 0, 0, 0, 0
    while i < n and j < n:
        if a[i] < d[j]:
            m += 1
            mi = max(m, mi)
            i += 1
        else:
            m -= 1
            j += 1
    print mi
