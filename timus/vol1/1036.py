import sys


def main():
    n, s = map(int, sys.stdin.readline().split())
    if s % 2 == 1:
        return 0
    t = s // 2
    dp = [[0 for _ in range(t+1)] for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n+1):
        for j in range(t+1):
            for k in range(min(9, j)+1):
                dp[i][j] += dp[i-1][j-k]
    return dp[n][t] ** 2

print(main())
