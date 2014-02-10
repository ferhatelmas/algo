class Archery:
    def expectedPoints(self, N, ringPoints):
        return sum(i*r for i, r in zip(xrange(1, 2*(N+1), 2), ringPoints)) / \
            float(sum(xrange(1, 2*(N+1), 2)))
