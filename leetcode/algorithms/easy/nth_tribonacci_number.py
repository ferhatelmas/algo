class Solution:
    def tribonacci(self, n: int) -> int:
        ls = [0, 1, 1]
        for i in range(3, n + 1):
            ls.append(ls[i - 3] + ls[i - 2] + ls[i - 1])
        return ls[n]
