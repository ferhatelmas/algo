from collections import Counter
from string import ascii_lowercase


class Solution:
    def equalFrequency(self, word: str) -> bool:
        d = Counter(word)
        for c in ascii_lowercase:
            if c not in d:
                continue
            d[c] -= 1
            s = set(d[c2] for c2 in ascii_lowercase if c2 in d and d[c2] > 0)
            if len(s) == 1:
                return True
            d[c] += 1
        return False
