class ProfitCalculator:
    def percent(self, items):
        p, c = reduce(lambda (x, y), (a, b): (x+float(a), y+float(b)),
                      map(lambda i: i.split(), items), [0, 0])
        return int((p-c) / p * 100)
