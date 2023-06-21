from operator import itemgetter
from typing import List


class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        score.sort(key=itemgetter(k), reverse=True)
        return score
