from typing import List
from itertools import permutations


class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        s = set()
        for a, b, c in permutations(digits, 3):
            if a != 0 and c % 2 == 0:
                s.add(100 * a + 10 * b + c)
        return len(s)
