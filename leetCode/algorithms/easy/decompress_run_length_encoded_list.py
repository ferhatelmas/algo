from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ls = []
        for i in range(0, len(nums), 2):
            ls.extend([nums[i + 1]] * nums[i])
        return ls
