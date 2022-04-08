class Solution:
    def calculate(self, s):
        ls, res, c, l, ll, i = [], 0, 1, 1, len(s), 0
        while i < ll:
            e, i = s[i], i + 1
            if e == "-":
                l = -1
            elif e == "(":
                c *= l
                ls.append(l)
                l = 1
            elif e == ")":
                c *= ls.pop()
            elif e not in " +":
                while i < ll and "0" <= s[i] <= "9":
                    e += s[i]
                    i += 1
                res += int(e) * c * l
                l = 1
        return res
