from collections import Counter
from itertools import chain
from typing import List


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        return chain(
            *(
                [k] * v
                for k, v in sorted(Counter(nums).items(), key=lambda x: (x[1], -x[0]))
            )
        )
