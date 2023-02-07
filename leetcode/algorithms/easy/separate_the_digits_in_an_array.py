from itertools import chain
from typing import List


class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return [int(e) for e in chain(*(list(str(n)) for n in nums))]
