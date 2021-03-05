class KDoubleSubstrings:
    def howMuch(self, str, k):
        def diff(a, b):
            return len(filter(lambda (e, f): e != f, zip(a, b)))

        s = "".join(str)
        l, c = len(s), 0
        for i in xrange(1, l / 2 + 1):
            for j in xrange(l - 2 * i + 1):
                if diff(s[j : j + i], s[j + i : j + 2 * i]) <= k:
                    c += 1
        return c
