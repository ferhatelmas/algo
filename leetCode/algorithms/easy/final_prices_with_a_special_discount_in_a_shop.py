from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ls = []
        for i, e in enumerate(prices):
            discount = 0
            for j in prices[i + 1 :]:
                if j <= e:
                    discount = j
                    break
            ls.append(e - discount)
        return ls
