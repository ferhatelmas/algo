class RaiseThisBarn:
    def calc(self, str):
        if str.count('c')%2:
            return 0
        return sum(str[:i].count('c') == str[i:].count('c')
                   for i in xrange(1, len(str)))
