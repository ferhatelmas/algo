class Palindromize2:
    def minChanges(self, s):
        return "".join([min(s[i], s[-i - 1]) for i in xrange(len(s))])
