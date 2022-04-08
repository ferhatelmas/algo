from bisect import bisect_left


class Solution:
    def searchInsert(self, A, target):
        return bisect_left(A, target)
