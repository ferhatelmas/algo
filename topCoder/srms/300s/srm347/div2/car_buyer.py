class CarBuyer:
    def lowestCost(self, cars, fuelPrice, annualDistance, years):
        cs, d = [], float(annualDistance * years)
        for c, t, e in map(lambda c: map(int, c.split()), cars):
            cs.append(c + t * years + (fuelPrice * d / e))
        return sorted(cs)[0]
