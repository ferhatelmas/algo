from typing import List


class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        c = 0
        for i, a in enumerate(hours):
            for b in hours[i + 1 :]:
                print(a + b)
                c += (a + b) % 24 == 0
        return c
