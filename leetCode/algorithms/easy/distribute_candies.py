class Solution(object):
    def distributeCandies(self, candies):
        n = len(set(candies))
        k = len(candies) / 2
        return k if n > k else n
