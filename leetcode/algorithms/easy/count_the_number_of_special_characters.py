class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s, d = set(), {}
        for e in word:
            if e in s:
                continue
            s.add(e)
            v = e.lower()
            if v in d:
                if v == e:
                    d[v] -= 1
                else:
                    d[v] += 1
            else:
                if v == e:
                    d[v] = -1
                else:
                    d[v] = 1
        return sum(v == 0 for v in d.values())
