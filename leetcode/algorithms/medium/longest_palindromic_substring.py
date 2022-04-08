class Solution:
    def longestPalindrome(self, s):
        l = len(s)
        if l < 2:
            return s
        t = (0, -1)
        for i in range(l - 1):
            t = max(t, self.extend(s, i, i, l), self.extend(s, i, i + 1, l))
        return s[t[1] : t[1] + t[0]]

    def extend(self, s, j, k, l):
        while j >= 0 and k < l and s[j] == s[k]:
            j, k = j - 1, k + 1
        return k - j - 1, j + 1
