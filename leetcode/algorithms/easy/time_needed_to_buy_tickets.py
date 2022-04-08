from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        t = 0

        while tickets[k] > 0:
            for i, v in enumerate(tickets):
                if v > 0:
                    t += 1
                tickets[i] = v - 1
                if i == k and v == 1:
                    break
        return t
