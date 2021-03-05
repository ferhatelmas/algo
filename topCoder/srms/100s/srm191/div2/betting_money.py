class BettingMoney:
    def moneyMade(self, amounts, centsPerDollar, finalResult):
        return sum(
            map(
                lambda (i, (a, c)): -a * c if finalResult == i else a * 100,
                enumerate(zip(amounts, centsPerDollar)),
            )
        )
