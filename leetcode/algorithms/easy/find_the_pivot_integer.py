class Solution:
    def pivotInteger(self, n: int) -> int:
        c, s = 0, (n * (n + 1)) / 2
        for i in range(1, n + 1):
            c += i
            if s - c + i == c:
                return i
        return -1
