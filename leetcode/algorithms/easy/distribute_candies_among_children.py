class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        c = 0
        for i in range(min(n, limit) + 1):
            a = n - i
            for j in range(min(a, limit) + 1):
                c += 0 <= a - j <= limit
        return c
