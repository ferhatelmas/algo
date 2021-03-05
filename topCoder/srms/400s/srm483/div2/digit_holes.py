class DigitHoles:
    def numHoles(self, number):
        d = {"12357": 0, "0469": 1, "8": 2}
        return sum(v for e in str(number) for k, v in d.iteritems() if e in k)
