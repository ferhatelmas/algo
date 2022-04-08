from operator import itemgetter
from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        return "".join(e for e, i in sorted(zip(s, indices), key=itemgetter(1)))
