import math


class Solution(object):
    def constructRectangle(self, area):
        l = int(math.ceil(area ** 0.5))
        while area % l > 0:
            l += 1
        return (l, area / l)
