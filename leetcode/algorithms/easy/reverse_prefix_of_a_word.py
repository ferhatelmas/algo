class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i, e in enumerate(word):
            if e == ch:
                return word[: i + 1][::-1] + word[i + 1 :]
        return word
