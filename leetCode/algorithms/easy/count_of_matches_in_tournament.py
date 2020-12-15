class Solution:
    def numberOfMatches(self, n: int) -> int:
        cnt = 0
        while n > 1:
            if n % 2 == 0:
                d = n // 2
                n = d
            else:
                d = (n - 1) // 2
                n = d + 1
            cnt += d
        return cnt
