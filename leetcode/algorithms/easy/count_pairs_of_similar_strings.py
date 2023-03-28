from typing import List


class Solution:
    def similarPairs(self, words: List[str]) -> int:
        n = 0
        for i, w in enumerate(words):
            s = set(w)
            for w2 in words[i + 1 :]:
                if not s.symmetric_difference(set(w2)):
                    n += 1
        return n
