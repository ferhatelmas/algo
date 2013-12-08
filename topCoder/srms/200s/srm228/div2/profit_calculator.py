class ProfitCalculator:
    def percent(self, items):
        p, c = map(sum, zip(*map(lambda i: map(float, i.split()), items)))
        return int((p - c) * 100 / p)
