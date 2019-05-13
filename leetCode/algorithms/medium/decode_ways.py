class Solution:
    m = {}

    def numDecodings(self, s):
        if not s:
            return 0
        return self.decode(s, len(s))

    def decode(self, s, l):
        if s[:1] == '0':
            return 0
        if l < 2:
            return 1
        if s in self.m:
            return self.m[s]
        n = self.decode(s[1:], l - 1)
        if 0 < int(s[:2]) <= 26:
            n += self.decode(s[2:], l - 2)
        self.m[s] = n
        return n
