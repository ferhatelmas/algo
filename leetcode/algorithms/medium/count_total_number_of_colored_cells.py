class Solution:
    def coloredCells(self, n: int) -> int:
        if n == 1:
            return n
        return 1 + sum(4 * (i - 1) for i in range(2, n + 1))
