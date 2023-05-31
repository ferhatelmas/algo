from typing import List


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        n = prices[0] + prices[1]
        return money if n > money else money - n
