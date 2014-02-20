class CircleMarket:
    def makePurchases(self, openTime, closeTime, travelTime):
        s, r, m, t, l = 0, 0, max(closeTime), set(), len(openTime)
        while s <= m and r < l:
            for i, (o, c) in enumerate(zip(openTime, closeTime)):
                if o <= s <= c and i not in t:
                    r += 1
                    t.add(i)
                s += travelTime
        return r
