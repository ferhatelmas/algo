import re

class MixtureDensity:
    def getDensity(self, ingredients):
        d, v = 0.0, 0
        for i in ingredients:
            m = re.match(r'(\d+) ml of [\w\s]+, weighing (\d+) g', i)
            v += int(m.group(1))
            d += int(m.group(2))
        return d/v
