class Solution:
    def minOperations(self, n: int) -> int:
        ls = [2 * i + 1 for i in range(0, n)]
        k = sum(ls) / n
        return sum(abs(k - e) for e in ls) // 2
