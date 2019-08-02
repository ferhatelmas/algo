class Solution:

    ns = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

    def romanToInt(self, s):
        s = (
            s.replace("CM", "DCCCC")
            .replace("CD", "CCCC")
            .replace("XC", "LXXXX")
            .replace("XL", "XXXX")
            .replace("IX", "VIIII")
            .replace("IV", "IIII")
        )
        return sum(self.ns[e] for e in s)
