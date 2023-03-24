from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        ns, ne = -1, -1
        ps, pe = -1, -1
        for i, e in enumerate(nums):
            if e > 0:
                if ns == -1:
                    ns = i
                ne = max(i, ne)
            elif e < 0:
                if ps == -1:
                    ps = i
                pe = max(i, pe)
        nd = ne - ns + 1 if ne > -1 else 0
        pd = pe - ps + 1 if pe > -1 else 0
        return max(nd, pd)
