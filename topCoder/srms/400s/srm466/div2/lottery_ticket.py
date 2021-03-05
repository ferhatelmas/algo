from itertools import combinations


class LotteryTicket:
    def buy(self, price, b1, b2, b3, b4):
        l = [b1, b2, b3, b4]
        for i in xrange(1, 5):
            for e in combinations(l, i):
                if sum(e) == price:
                    return "POSSIBLE"
        return "IMPOSSIBLE"
