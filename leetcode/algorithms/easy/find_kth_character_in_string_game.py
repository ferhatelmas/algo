from string import ascii_lowercase


class Solution:
    def kthCharacter(self, k: int) -> str:
        d = {a: b for a, b in zip(ascii_lowercase, ascii_lowercase[1:] + "a")}
        l, w = 1, ["a"]
        while l < k:
            for e in w[:l]:
                w.append(d[e])
            l *= 2
        return w[k - 1]
