class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        d1, d2 = "", ""
        for a, b in zip(s1, s2):
            if a != b:
                d1, d2 = d1 + a, d2 + b
        return len(d1) in [0, 2] and sorted(d1) == sorted(d2)
