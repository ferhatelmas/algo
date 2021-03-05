class TwiceString:
    def getShortest(self, s):
        l = len(s)
        i = l - 1
        while i > 0 and s[:i] != s[l - i :]:
            i -= 1
        return s + s[i:]
