class Solution:
    def numSplits(self, s: str) -> int:
        li, ri = [0] * 26, [0] * 26
        for e in s:
            ri[ord(e) - ord("a")] += 1

        result, l, r = 0, 0, sum(e > 0 for e in ri)
        for e in s:
            j = ord(e) - ord("a")
            ri[j] -= 1
            if ri[j] == 0:
                r -= 1

            if li[j] == 0:
                l += 1
            li[j] += 1

            if l == r:
                result += 1
        return result
