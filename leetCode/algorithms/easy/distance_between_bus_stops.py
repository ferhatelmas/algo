from typing import List


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], a: int, b: int) -> int:
        n = sum(distance)
        cw = sum(distance[min(a, b) : max(a, b)])
        return min(cw, n - cw)
