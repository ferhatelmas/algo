class Solution:
    def search(self, nums, target):
        i, l = 0, len(nums) - 1
        while i <= l:
            m = i + (l - i) / 2
            if nums[m] == target:
                return True
            elif nums[i] == nums[m]:
                i += 1
            elif nums[l] == nums[m]:
                l -= 1
            elif nums[i] <= target <= nums[m]:
                l = m
            elif nums[m] < target <= nums[l]:
                i = m + 1
            elif nums[i] > nums[m]:
                l = m
            else:
                i = m + 1
        return False
