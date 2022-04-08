from string import ascii_lowercase


class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        ss, s = set(), ""
        for e in word:
            if e in ascii_lowercase:
                if s:
                    ss.add(int(s))
                    s = ""
            else:
                s += e
        if s:
            ss.add(int(s))
        return len(ss)
