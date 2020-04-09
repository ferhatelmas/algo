from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        ns, s = sorted(nums), sum(nums)
        res, cnt = [], 0
        for e in reversed(ns):
            if cnt > s - cnt:
                break
            res.append(e)
            cnt += e
        return res
