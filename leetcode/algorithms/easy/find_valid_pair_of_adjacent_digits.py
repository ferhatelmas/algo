from collections import Counter


class Solution:
    def findValidPair(self, s: str) -> str:
        c = Counter(s)
        for i, e in enumerate(s):
            if i == 0:
                continue
            f = s[i - 1]
            if e == f:
                continue
            if c[e] == int(e) and c[f] == int(f):
                return f + e
        return ""
