class Solution:
    def longestConsecutive(self, nums):
        nums, best = set(nums), 0
        for n in nums:
            if n - 1 not in nums:
                m = n + 1
                while m in nums:
                    m += 1
                best = max(best, m - n)
        return best
