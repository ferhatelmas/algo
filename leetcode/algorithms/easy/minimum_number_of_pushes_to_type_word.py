from collections import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:
        return sum(i // 8 + 1 for i, _ in enumerate(Counter(word).most_common()))
