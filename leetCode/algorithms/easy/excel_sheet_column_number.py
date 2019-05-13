class Solution:
    def titleToNumber(self, s):
        l = len(s)
        return sum(
            26**(l - i) * (1 + ord(e) - ord('A')) for i, e in enumerate(s, 1))
