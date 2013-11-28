class LCMRange:
    def lcm(self, first, last):
        def cnt(n, p):
            c = 0
            while n%p == 0:
                c += 1
                n /= p
            return c

        p, v = [2, 3, 5, 7, 11], [0]*5
        for x in xrange(first, last+1):
            for i in range(5):
                v[i]= max(v[i], cnt(x, p[i]))
        return reduce(lambda x, y: x*y, map(lambda (pr, pw): pr**pw, zip(p, v)))
