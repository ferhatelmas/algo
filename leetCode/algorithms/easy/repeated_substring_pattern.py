class Solution(object):
    def repeatedSubstringPattern(self, str):
        l = len(str)
        return any(l % k == 0 and str[:k] * (l / k) == str for k in range(l / 2, 0, -1))
