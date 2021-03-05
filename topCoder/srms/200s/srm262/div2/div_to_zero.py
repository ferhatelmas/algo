class DivToZero:
    def lastTwo(self, num, factor):
        b = str(num)[:-2]
        for i in xrange(100):
            s = str(i)
            if i < 10:
                s = "0" + s
            if int(b + s) % factor == 0:
                return s
