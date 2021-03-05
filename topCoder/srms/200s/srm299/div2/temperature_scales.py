class TemperatureScales:
    def convert(self, f1, b1, f2, b2, t):
        return float(t - f1) * (b2 - f2) / (b1 - f1) + f2
