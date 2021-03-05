class CheckFunction:
    def newFunction(self, code):
        m = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
        return sum(map(lambda c: m[ord(c) - ord("0")], code))
