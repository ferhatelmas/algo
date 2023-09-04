class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def is_symmetric(n):
            s = str(n)
            l = len(s)
            if l % 2:
                return False
            l = l // 2
            ls = [int(e) for e in s]
            return sum(ls[:l]) == sum(ls[l:])

        return sum(is_symmetric(n) for n in range(low, high + 1))
