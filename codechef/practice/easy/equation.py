# Time limit
for _ in range(int(input())):
    n, a, b, c = map(int, input().split())

    cnt = 0
    for i in range(a + 1):
        for j in range(min(b, n - i) + 1):
            cnt += min(c, n - i - j) + 1
    print(cnt)
