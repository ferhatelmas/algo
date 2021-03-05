class ShippingCubes:
    def minimalCost(self, N):
        m = 600
        for i in xrange(1, 200):
            for j in xrange(1, i + 1):
                for k in xrange(1, j + 1):
                    if i * j * k == N:
                        m = min(m, i + j + k)
        return m
