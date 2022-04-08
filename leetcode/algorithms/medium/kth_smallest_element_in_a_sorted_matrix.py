import heapq


class Solution(object):
    def kthSmallest(self, matrix, k):
        return max(heapq.nsmallest(k, heapq.merge(*matrix)))
