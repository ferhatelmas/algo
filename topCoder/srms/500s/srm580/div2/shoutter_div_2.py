class ShoutterDiv2:
    def count(self, s, t):
        c = 0
        for n, (i, j) in enumerate(zip(s, t)):
            for k, l in zip(s[n + 1 :], t[n + 1 :]):
                if i <= k <= j or k <= i <= l:
                    c += 1
        return c
