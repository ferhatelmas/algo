from heapq import heapify, heappop, heappush


class TheJackpotDivTwo:
    def find(self, money, jackpot):
        h = list(money)
        heapify(h)
        while jackpot:
            heappush(h, heappop(h) + 1)
            jackpot -= 1
        return [heappop(h) for i in xrange(len(h))]
