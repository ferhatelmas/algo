class EqualSubstrings:
    def getSubstrings(self, str):
        def is_fine(x, y):
            return x.count('a') == y.count('b')
        for i in xrange(len(str), 0, -1):
            x, y = str[0:i], str[i:]
            if is_fine(x, y):
                return x, y
        return '', str
