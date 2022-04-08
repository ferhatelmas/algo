from typing import List


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        t, s = 0, 0
        for a, d in customers:
            s, t = s + max(t - a, 0) + d, max(a, t) + d
        return s / len(customers)
