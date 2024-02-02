from typing import List


class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        t, cur = 0, capacity
        for i, n in enumerate(plants):
            if cur < n:
                cur = capacity - n
                t += 2 * (i + 1) - 1
            else:
                cur -= n
                t += 1
        return t
