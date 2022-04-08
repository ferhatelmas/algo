from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for n, i in zip(nums, index):
            target.insert(i, n)
        return target
