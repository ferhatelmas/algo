class EratosthenSieve2:
    def nthElement(self, n):
        ns = range(1, 1000)
        for i in range(2, 11):
            ns = [e for j, e in enumerate(ns, 1) if j % i != 0]
        return ns[n - 1]
