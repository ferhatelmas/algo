from itertools import chain, filterfalse
from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        def odd(x):
            return x % 2

        return list(chain(filterfalse(odd, A), filter(odd, A)))
