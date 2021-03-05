class PersistentNumber:
    def getPersistence(self, n):
        def p(x):
            return reduce(lambda a, e: a * int(e), str(x), 1)

        i = 0
        while n > 9:
            i += 1
            n = p(n)
        return i
