class Solution:
    def sumBase(self, n: int, k: int) -> int:
        c = 0
        while n > 0:
            n, remainder = divmod(n, k)
            c += remainder

        return c
