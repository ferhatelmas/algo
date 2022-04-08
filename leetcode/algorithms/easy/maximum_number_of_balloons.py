class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counts = {"b": 0, "a": 0, "l": 0, "o": 0, "n": 0}
        for e in text:
            if e in counts:
                counts[e] += 1
        ones = min(counts[e] for e in "ban")
        doubles = min(counts[e] // 2 for e in "lo")
        return min(ones, doubles)
