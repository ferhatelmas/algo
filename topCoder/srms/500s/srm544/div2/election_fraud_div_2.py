class ElectionFraudDiv2:
    def IsFraudulent(self, percentages):
        ra, rb = 0, 0
        for p in percentages:
            a, b = 10001, 0
            for i in xrange(10001):
                if int(round(i * 100.0 / 10000)) == p:
                    a, b = min(a, i), max(b, i)
            if not b:
                return "YES"
            ra += a
            rb += b
        return "NO" if ra <= 10000 <= rb else "YES"
