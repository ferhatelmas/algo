from math import ceil

class Inventory:
    def monthlyOrder(self, sales, daysAvailable):
        ls = [s * 30.0 / d
              for s, d in zip(sales, daysAvailable)
              if d > 0]
        return int(ceil(sum(ls) / len(ls) - 10**-9))
