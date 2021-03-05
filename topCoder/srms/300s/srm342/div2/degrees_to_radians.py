from math import pi


class DegreesToRadians:
    def convertToRadians(self, degrees, minutes, seconds):
        c = degrees + minutes / 60.0 + seconds / 3600.0
        return c * pi / 180
