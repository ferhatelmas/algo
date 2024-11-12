class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def product(n):
            res = 1
            for e in str(n):
                res *= int(e)
            return res

        while product(n) % t:
            n += 1
        return n
