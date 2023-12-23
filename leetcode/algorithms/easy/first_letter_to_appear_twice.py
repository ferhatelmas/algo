class Solution:
    def repeatedCharacter(self, s: str) -> str:
        d = set()
        for e in s:
            if e in d:
                return e
            d.add(e)
        return None
