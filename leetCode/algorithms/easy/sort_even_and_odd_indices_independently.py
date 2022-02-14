from itertools import chain, zip_longest
from typing import List


class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even = nums[0::2]
        odd = nums[1::2]

        even.sort()
        odd.sort(reverse=True)
        ls = list(chain(*zip_longest(even, odd, fillvalue=None)))
        if ls and ls[-1] is None:
            return ls[:-1]
        return ls
