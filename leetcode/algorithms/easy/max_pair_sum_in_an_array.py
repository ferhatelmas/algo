from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        def maxDigit(d: int) -> int:
            return max(int(e) for e in str(d))

        m = -1
        for i, a in enumerate(nums[:-1]):
            aa = maxDigit(a)
            for b in nums[i + 1 :]:
                bb = maxDigit(b)
                print(a, b, aa, bb)
                if aa == bb:
                    m = max(m, a + b)
        return m


print(Solution().maxSum([31, 25, 72, 79, 74]))
