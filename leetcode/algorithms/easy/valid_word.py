from string import ascii_lowercase, digits


class Solution:
    def isValid(self, word: str) -> bool:
        v, c = False, False
        for e in word.lower():
            if e not in ascii_lowercase and e not in digits:
                return False

            if not v and e in "aeiou":
                v = True
                continue

            if not c and e in ascii_lowercase and e not in "aeiou":
                c = True
                continue

        return v and c and len(word) >= 3
