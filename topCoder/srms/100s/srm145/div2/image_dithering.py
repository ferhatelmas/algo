class ImageDithering:
    def count(self, dithered, screen):
        return sum(map(lambda e: sum(map(lambda x: x in dithered, e)), screen))
