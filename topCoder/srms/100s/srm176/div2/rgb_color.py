class RGBColor:
    def getComplement(self, rgb):
        if any(map(lambda r: abs(255 - 2 * r) > 32, rgb)):
            return [255 - r for r in rgb]
        return [(r + 128) % 256 for r in rgb]
