from typing import List


class Solution:
    def findIndices(
        self, nums: List[int], indexDifference: int, valueDifference: int
    ) -> List[int]:
        for i, a in enumerate(nums):
            for j, b in enumerate(nums[i + indexDifference :]):
                if abs(a - b) >= valueDifference:
                    return [i, i + j + indexDifference]
        return [-1, -1]
