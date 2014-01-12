from operator import mul

class MultiNumber:
    def check(self, number):
        s = str(number)
        def e(a, b):
            def do_e(x):
                return reduce(mul, map(int, x))
            return do_e(a) == do_e(b)
        return 'YES' if any(e(s[:i], s[i:]) for i in xrange(1, len(s))) else 'NO'
