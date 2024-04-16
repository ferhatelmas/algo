class Solution:
    def findLatestTime(self, s: str) -> str:
        r = ""
        for i, e in enumerate(s):
            if e != "?" or e == ":":
                r += e
                continue
            if i == 0:
                r += "1" if s[1] in "?01" else "0"
            elif i == 1:
                r += "1" if r[0] == "1" else "9"
            elif i == 3:
                r += "5"
            else:
                r += "9"
        return r
