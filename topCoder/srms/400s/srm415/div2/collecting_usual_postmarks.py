class CollectingUsualPostmarks:
    def numberOfPostmarks(self, prices, have):
        m = sum([prices[i] for i in have])
        i, l, prices = 0, len(prices), sorted(prices)
        while i < l and m >= prices[i]:
            m -= prices[i]
            i += 1
        return i
