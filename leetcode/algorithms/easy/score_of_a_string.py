class Solution:
    def scoreOfString(self, s: str) -> int:
        c = 0
        for i, e in enumerate(s):
            if i == 0:
                continue
            c += abs(ord(s[i - 1]) - ord(e))
        return c
