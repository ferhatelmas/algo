from typing import List


class Solution:
    def dietPlanPerformance(
        self, calories: List[int], k: int, lower: int, upper: int
    ) -> int:
        points, s = 0, sum(calories[: k - 1])
        for i in range(k - 1, len(calories)):
            s += calories[i]
            if i >= k:
                s -= calories[i - k]
            if s > upper:
                points += 1
            elif s < lower:
                points -= 1

        return points
