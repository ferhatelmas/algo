# TODO: better algorithm
class Solution:
    def maxSlidingWindow(self, nums, k):
        if not nums:
            return []
        return [max(nums[i:i + k]) for i in range(len(nums) - k + 1)]
