class Solution(object):
    def hIndex(self, citations):
        l = len(citations)
        ls, r = [0] * (l + 1), 0
        for e in citations:
            ls[min(e, l)] += 1
        while l > -1:
            r += ls[l]
            if r >= l:
                return l
            l -= 1
