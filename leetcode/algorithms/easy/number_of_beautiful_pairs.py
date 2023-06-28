from typing import List


class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        def gcd(a, b) -> int:
            for i in range(2, min(a, b) + 1):
                if a % i == 0 and b % i == 0:
                    return i
            return 1

        return sum(
            gcd(int(str(a)[0]), b % 10) == 1
            for i, a in enumerate(nums)
            for b in nums[i + 1 :]
        )
