from typing import List


class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        return sum(
            (sum(nums[: i + 1]) - sum(nums[i + 1 :])) % 2 == 0
            for i in range(0, len(nums) - 1)
        )
