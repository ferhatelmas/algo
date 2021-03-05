class FoxAndGame:
    def countStars(self, result):
        return sum(r.count("o") for r in result)
