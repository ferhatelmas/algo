class EggCartons:
    def minCartons(self, n):
        d = {}
        for i in xrange(17):
            for j in xrange(13):
                c = 6*i + 8*j
                d[c] = min(i+j, d.get(c, 30))
        return d[n] if n in d else -1
