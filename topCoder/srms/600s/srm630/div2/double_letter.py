class DoubleLetter:
    def ableToSolve(self, S):
        def remove(s):
            for k, (i, j) in enumerate(zip(s, s[1:])):
                if i == j:
                    return s[:k] + s[k + 2 :]
            return s

        while True:
            s = remove(S)
            if S == s:
                break
            S = s
        return "Possible" if not S else "Impossible"
