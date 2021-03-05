class BigBurger:
    def maxWait(self, arrival, service):
        t, m = 0, 0
        for i, (a, s) in enumerate(zip(arrival, service)):
            if i == 0:
                t = a + s
            else:
                if t >= a:
                    m = max(m, t - a)
                    t += s
                else:
                    t = a + s
        return m
