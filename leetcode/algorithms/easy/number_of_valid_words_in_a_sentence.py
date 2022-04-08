import re

r = re.compile(r"^[a-z]*([a-z]+-[a-z]+)?[!,.]?$")


class Solution:
    def countValidWords(self, sentence: str) -> int:
        return sum(1 for word in sentence.split() if r.match(word))
