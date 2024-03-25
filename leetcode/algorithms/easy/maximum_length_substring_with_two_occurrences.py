from collections import Counter


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l, m = len(s), 0
        for i in range(l, 0, -1):
            for j in range(l - i + 1):
                if i <= m:
                    continue
                c = Counter(s[j : j + i])
                if c.most_common(1)[0][1] <= 2:
                    m = max(m, i)
        return m
