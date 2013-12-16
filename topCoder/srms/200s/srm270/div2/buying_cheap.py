class BuyingCheap:
    def thirdBestPrice(self, prices):
        ls = sorted(set(prices))
        return -1 if len(ls) < 3 else ls[2]
