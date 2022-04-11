from typing import List


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res, inc, index = [0] * num_people, 1, 0
        while candies > 0:
            res[index] += min(inc, candies)
            index, inc, candies = (index + 1) % num_people, inc + 1, candies - inc
        return res
