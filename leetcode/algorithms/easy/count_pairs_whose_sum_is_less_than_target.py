from typing import List


class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        cnt = 0
        for i, a in enumerate(nums[:-1]):
            for b in nums[i + 1 :]:
                if a + b < target:
                    cnt += 1
        return cnt
