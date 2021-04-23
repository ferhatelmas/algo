from string import ascii_lowercase


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s, l = set(ascii_lowercase), len(ascii_lowercase)
        for e in sentence:
            if e in s:
                s.remove(e)
                l -= 1
                if l == 0:
                    return True
        return False
