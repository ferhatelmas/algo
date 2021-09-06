from typing import List


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        cnt = 0
        for i, a in enumerate(nums):
            for j, b in enumerate(nums[i + 1 :]):
                for k, c in enumerate(nums[i + j + 2 :]):
                    for d in nums[i + j + k + 3 :]:
                        cnt += a + b + c == d
        return cnt
