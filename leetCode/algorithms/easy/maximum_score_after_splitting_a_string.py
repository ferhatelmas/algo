class Solution:
    def maxScore(self, s: str) -> int:
        one, zero, m = sum(e == "1" for e in s), 0, 0
        for e in s[:-1]:
            if e == "0":
                zero += 1
            else:
                one -= 1
            m = max(m, one + zero)
        return m
