from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        l, s, k = len(nums), set(), -1
        for i in range(l - 1, -1, -1):
            if nums[i] in s:
                k = i
                break
            s.add(nums[i])

        n, m = divmod(k + 1, 3)
        if m:
            n += 1
        return n
