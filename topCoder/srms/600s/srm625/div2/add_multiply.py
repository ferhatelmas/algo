class AddMultiply:
    def makeExpression(self, y):
        for i in xrange(-1000, 1001):
            if 0 <= i <= 1:
                continue
            for j in xrange(-1000, 1001):
                if 0 <= j <= 1:
                    continue
                for k in xrange(-1000, 1001):
                    if 0 <= k <= 1:
                        continue
                    if i * j + k == y:
                        return i, j, k
