from typing import List


class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        return sum(w == w2[::-1] for i, w in enumerate(words) for w2 in words[i + 1 :])
