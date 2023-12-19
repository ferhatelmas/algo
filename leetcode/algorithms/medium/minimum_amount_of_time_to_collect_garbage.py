from typing import List


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        s = 0
        for t in "MPG":
            last = 0
            for i, g in enumerate(garbage):
                c = g.count(t)
                s += c
                if c > 0:
                    last = i
            s += sum(travel[:last])
        return s
