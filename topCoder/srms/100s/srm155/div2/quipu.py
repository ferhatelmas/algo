class Quipu:
    def readKnots(self, knots):
        return "".join(map(str, map(len, knots[1:-1].split("-"))))
