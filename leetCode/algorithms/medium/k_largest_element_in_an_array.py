class Solution:
    def findKthLargest(self, nums, k):
        return sorted(nums, reverse=True)[k-1]
