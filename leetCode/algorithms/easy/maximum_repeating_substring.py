class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        m = len(sequence) // len(word)
        for i in range(m, -1, -1):
            if (i * word) in sequence:
                return i
        return 0
