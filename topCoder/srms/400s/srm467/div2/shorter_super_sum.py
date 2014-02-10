class ShorterSuperSum:
    def calculate(self, k, n):
        c = {}
        def s(kk, nn):
            if (kk, nn) in c:
                return c[(kk, nn)]
            if kk== 0:
                return nn
            c[(kk, nn)] = sum(s(kk-1, i) for i in xrange(1, nn+1))
            return c[(kk, nn)]
        return s(k, n)
