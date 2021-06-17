from typing import List


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        d = {}
        for word in words:
            for w in word:
                d[w] = d.get(w, 0) + 1
        l = len(words)
        return all(v % l == 0 for _, v in d.items())
