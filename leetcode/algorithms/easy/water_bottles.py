class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        s = numBottles
        while numBottles > 0:
            a, b = divmod(numBottles, numExchange)
            if a == 0:
                return s
            s += a
            numBottles = a + b
