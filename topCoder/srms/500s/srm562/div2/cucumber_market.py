from itertools import combinations

class CucumberMarket:
    def check(self, price, budget, k):
        for e in combinations(price, k):
            if sum(e) > budget:
                return 'NO'
        return 'YES'
