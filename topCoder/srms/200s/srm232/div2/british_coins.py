class BritishCoins:
    def coins(self, pence):
        return [pence / 240, (pence % 240) / 12, pence % 12]
