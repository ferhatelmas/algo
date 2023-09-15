from string import ascii_lowercase


class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        i, d = 0, {}
        for e in key:
            if e not in d and e != " ":
                d[e] = ascii_lowercase[i]
                i += 1
        return "".join(d.get(e, " ") for e in message)
