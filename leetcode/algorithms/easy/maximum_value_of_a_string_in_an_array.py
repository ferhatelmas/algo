from string import digits
from typing import List


class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        def val(s: str) -> int:
            if all(e in digits for e in s):
                return int(s)
            return len(s)

        return max(val(s) for s in strs)
