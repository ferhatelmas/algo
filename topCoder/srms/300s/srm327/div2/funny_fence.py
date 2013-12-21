class FunnyFence:
    def getLength(self, s):
        p, c, m = '', 0, 0
        for e in s:
            if e == p:
                m = max(m, c)
                c = 0
            c += 1
            p = e
        return max(m, c)
