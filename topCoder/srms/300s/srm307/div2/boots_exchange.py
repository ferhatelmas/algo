class BootsExchange:
    def leastAmount(self, left, right):
        l, r = {}, {}
        for a, b in zip(left, right):
            l[a] = l.get(a, 0) + 1
            r[b] = r.get(b, 0) + 1
        return sum(map(lambda k: max(l[k] - r.get(k, 0), 0), l.keys()))
