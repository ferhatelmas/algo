class Solution:
    def removeInvalidParentheses(self, s):
        r = []
        self.remove(s, r, 0, 0, "()")
        return r

    def remove(self, s, r, li, lj, c):
        cnt = 0
        for i, e in enumerate(s[li:], start=li):
            cnt += (1, -1, 0)[c.find(e)]
            if cnt < 0:
                for j, f in enumerate(s[lj:i + 1], start=lj):
                    if f == c[1] and (j == lj or s[j - 1] != c[1]):
                        self.remove(s[:j] + s[j + 1:], r, i, j, c)
                return
        if c[0] == "(":
            self.remove(s[::-1], r, 0, 0, ")(")
        else:
            r.append(s[::-1])
