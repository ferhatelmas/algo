class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def in_base(n, m):
            ls = []
            while n:
                n, r = divmod(n, m)
                ls.append(r)
            return ls == ls[::-1]

        return all(in_base(n, base) for base in range(2, n - 1))
