class SupermarketDiscount:
    def minAmount(self, goods):
        s, i, r, c = sorted(goods), 0, 0, 0
        while i < 3:
            r += s[i]
            if r >= 50:
                c += r-10
                r = 0
            i += 1
        return c + r
