from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        l = len(stones)
        h = [(-e, e) for e in stones]
        heapify(h)
        while l >= 2:
            _, x = heappop(h)
            _, y = heappop(h)
            if x == y:
                l -= 2
            else:
                diff = abs(x - y)
                heappush(h, (-diff, diff))
                l -= 1
        return h[0][1] if l == 1 else 0
