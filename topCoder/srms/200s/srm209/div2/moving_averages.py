class MovingAverages:
    def calculate(self, times, n):
        def as_second(s):
            h, m, s = map(int, s.split(':'))
            return h * 3600 + m * 60 + s
        s = map(as_second, times)
        return map(lambda i: sum(s[i:i+n])/n, xrange(len(times)-n+1))
