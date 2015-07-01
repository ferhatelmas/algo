class Solution:
    def singleNumber(self, nums):
        return (sum(set(nums))*3 - sum(nums)) / 2
