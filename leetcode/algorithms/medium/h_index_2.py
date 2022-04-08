class Solution:
    def hIndex(self, citations):
        l, h, m, ln = 0, len(citations) - 1, 0, len(citations)
        while l <= h:
            m = (l + h) / 2
            if citations[m] == ln - m:
                return citations[m]
            elif citations[m] > (ln - m):
                h = m - 1
            else:
                l = m + 1
        return ln - h - 1
