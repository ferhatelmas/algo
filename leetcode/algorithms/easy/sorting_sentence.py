class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        result = [""] * len(words)
        for w in words:
            result[int(w[-1]) - 1] = w[:-1]
        return " ".join(result)
