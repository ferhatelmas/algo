from string import ascii_lowercase


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        replacements = [c * k for c in ascii_lowercase]
        while True:
            prev = s
            for rep in replacements:
                s = s.replace(rep, "", 1)
            if prev == s:
                return s
