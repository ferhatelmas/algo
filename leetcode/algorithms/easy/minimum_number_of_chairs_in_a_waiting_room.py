class Solution:
    def minimumChairs(self, s: str) -> int:
        m, c = 0, 0
        for e in s:
            c = c + (1 if e == "E" else -1)
            m = max(m, c)
        return m
