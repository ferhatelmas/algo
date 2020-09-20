class Solution:
    def reorderSpaces(self, text: str) -> str:
        spaces = text.count(" ")
        words = [w for w in text.split(" ") if w]
        l = len(words)
        if l == 1:
            return words[0] + " " * spaces
        each, remaining = divmod(spaces, l - 1)
        return (" " * each).join(words) + (" " * remaining)
