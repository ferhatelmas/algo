from itertools import product
from typing import List


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        return [
            "".join(ls)
            for ls in product(
                *([e] if "0" <= e <= "9" else [e.lower(), e.upper()] for e in S)
            )
        ]
