from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        v = 0
        for i, a in enumerate(nums[:-2]):
            for j, b in enumerate(nums[i + 1 : -1]):
                for c in nums[i + 1 + j + 1 :]:
                    v = max(v, (a - b) * c)
        return v
