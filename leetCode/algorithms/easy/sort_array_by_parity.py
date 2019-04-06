from itertools import chain, filterfalse


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        odd = lambda x: x%2
        return list(chain(filterfalse(odd, A), filter(odd, A)))
