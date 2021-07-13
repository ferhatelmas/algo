from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums[0:0] = nums
        return nums
