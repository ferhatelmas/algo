class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        z, o, c = 0, 0, 0
        for i, e in enumerate(s):
            if e == "0":
                if o > 0:
                    c = max(c, min(z, o) * 2)
                    z = 1
                    o = 0
                else:
                    z += 1
            else:
                o += 1
        return max(c, min(z, o) * 2)
