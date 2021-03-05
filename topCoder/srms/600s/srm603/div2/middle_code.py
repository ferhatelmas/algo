class MiddleCode:
    def encode(self, s):
        t, l = "", len(s)
        while l:
            if l % 2:
                t += s[l / 2]
                s = s[: l / 2] + s[l / 2 + 1 :]
            else:
                if s[l / 2 - 1] < s[l / 2]:
                    t += s[l / 2 - 1]
                    s = s[: l / 2 - 1] + s[l / 2 :]
                else:
                    t += s[l / 2]
                    s = s[: l / 2] + s[l / 2 + 1 :]
            l -= 1
        return t
