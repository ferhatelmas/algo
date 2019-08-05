class Solution:
    def binaryGap(self, N: int) -> int:
        m, p = 0, 0
        for i, e in enumerate(bin(N)[2:]):
            if e == "1":
                m, p = max(m, i - p), i
        return m
