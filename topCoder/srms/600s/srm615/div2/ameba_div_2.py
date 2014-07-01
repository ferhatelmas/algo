class AmebaDiv2:
    def simulate(self, X, A):
        for g in X:
            if A == g:
                A *= 2
        return A
