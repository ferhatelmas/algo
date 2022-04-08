for _ in range(int(input())):
    n = int(input())
    a = sorted(map(int, input().split()))
    d = sorted(map(int, input().split()))

    i, j, m, mi = 0, 0, 0, 0
    while i < n and j < n:
        if a[i] < d[j]:
            m += 1
            mi = max(m, mi)
            i += 1
        else:
            m -= 1
            j += 1
    print(mi)
