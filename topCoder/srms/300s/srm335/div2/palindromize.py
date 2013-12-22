class Palindromize:
    def minAdds(self, s):
        for i in xrange(len(s)):
            r = s + s[:i][::-1]
            if r == r[::-1]:
                return r
