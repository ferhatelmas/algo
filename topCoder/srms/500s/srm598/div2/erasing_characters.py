class ErasingCharacters:
    def simulate(self, s):
        l, f = len(s), True
        while f:
            f = False
            for i in xrange(l-1):
                if s[i] == s[i+1]:
                    s = s[:i] + s[i+2:]
                    l -= 2
                    f = True
                    break
        return s
