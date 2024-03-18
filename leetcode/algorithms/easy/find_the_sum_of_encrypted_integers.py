from typing import List


class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        def encrypt(n: int) -> int:
            s = str(n)
            return int(str(max(s)) * len(s))

        return sum(encrypt(e) for e in nums)
