class Solution(object):
    def findUnsortedSubarray(self, nums):
        f = l = -1
        for i, (a, b) in enumerate(zip(sorted(nums), nums)):
            if a != b:
                if f == -1:
                    f = i
                l = i
        return 0 if f == -1 else l - f + 1
