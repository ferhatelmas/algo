class ThePalindrome:
    def find(self, s):
        l = len(s)
        for i in xrange(l):
            t = s + s[:i][::-1]
            if t == t[::-1]:
                return l + i
