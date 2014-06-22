class MinCostPalindrome:
    def getMinimum(self, s, oCost, xCost):
        c = 0
        for i in xrange(len(s)/2):
            e = ''.join(sorted(s[i] + s[-i-1]))
            print e
            if e == '?o':
                c += oCost
            elif e == '?x':
                c += xCost
            elif e == '??':
                c += 2 * min(oCost, xCost)
            elif e == 'ox':
                return -1
        return c
