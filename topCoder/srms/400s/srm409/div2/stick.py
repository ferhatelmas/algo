from heapq import heappop, heappush


class Stick:
    def pieces(self, x):
        s, l, c = 64, [64], 1
        while s > x:
            m = heappop(l) / 2
            heappush(l, m)
            s -= m
            if s < x:
                s += m
                heappush(l, m)
                c += 1
        return c
