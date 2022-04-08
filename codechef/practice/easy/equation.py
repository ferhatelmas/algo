# Time limit
for _ in xrange(int(raw_input())):
    n, a, b, c = map(int, raw_input().split())

    cnt = 0
    for i in xrange(a + 1):
        for j in xrange(min(b, n - i) + 1):
            cnt += min(c, n - i - j) + 1
    print cnt
