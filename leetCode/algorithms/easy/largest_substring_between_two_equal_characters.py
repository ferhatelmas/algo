class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        m = -1
        for i, e in enumerate(s):
            j = s.rfind(e)
            if j != -1 and j > i:
                m = max(m, j - i - 1)
        return m
