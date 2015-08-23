class Solution:
    def numDistinct(self, s, t):
        sl, tl = len(s), len(t)
        if not t or sl < tl:
            return 0
        if sl == tl:
            return (0, 1)[s == t]
        ls = [1] + [0] * tl
        for i in range(sl):
            for j in range(min(tl-1, i), -1, -1):
                ls[j+1] += (0, ls[j])[t[j] == s[i]]
        return ls[tl]
