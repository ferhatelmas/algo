class GameOfLifeDivTwo:
    def theSimulation(self, init, T):
        s, l = init, len(init)
        def r(i):
            def rr(ls):
                return '1' if ls.count('1') >= 2 else '0'
            if i == 0:
                return rr(s[-1:] + s[:2])
            elif i == l-1:
                return rr(s[-2:] + s[:1])
            else:
                return rr(s[i-1:i+2])
        while T:
            s = ''.join([r(i) for i in xrange(l)])
            T -= 1
        return s
