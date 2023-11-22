from typing import List


class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        pad = "0" * 32
        r, ls = 0, [bin(n)[2:][::-1] + pad for n in nums]
        for i in range(32):
            c = sum(l[i] == "1" for l in ls)
            if c >= k:
                r += 2**i
        return r
