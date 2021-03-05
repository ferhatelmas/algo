n, m = list(map(int, input().split()))

ls = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            ls[i][j] = 1
            continue
        if i > 0:
            ls[i][j] += ls[i - 1][j]
        if j > 0:
            ls[i][j] += ls[i][j - 1]
print(ls[n - 1][m - 1])
