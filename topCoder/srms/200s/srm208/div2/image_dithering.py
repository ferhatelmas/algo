class ImageDithering:
    def count(self, dithered, screen):
        return sum(map(lambda s: len(filter(lambda e: e in dithered, s)), screen))
