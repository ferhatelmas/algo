from collections import Counter
from typing import List


class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        return Counter(A).most_common(1)[0][0]
