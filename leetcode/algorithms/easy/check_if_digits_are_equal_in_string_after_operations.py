class Solution:
    def hasSameDigits(self, s: str) -> bool:
        l, ls = len(s), [int(c) for c in s]
        while l > 2:
            for i in range(0, l - 1):
                ls[i] = (ls[i] + ls[i + 1]) % 10
            ls = ls[:-1]
            l -= 1
        return ls[0] == ls[1]
