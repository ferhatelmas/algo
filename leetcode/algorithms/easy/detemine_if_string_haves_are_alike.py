class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        c, n = 0, len(s) // 2
        for i, e in enumerate(s):
            if e not in "aeiouAEIOU":
                continue

            if i < n:
                c += 1
            else:
                c -= 1
        return c == 0
