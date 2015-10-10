class Solution:
    def nextPermutation(self, nums):
        l = len(nums)
        for i in range(l-1, 0, -1):
            if nums[i-1] < nums[i]:
                nums[i:] = sorted(nums[i:])
                for j in range(i, l):
                    if nums[j] > nums[i-1]:
                        nums[j], nums[i-1] = nums[i-1], nums[j]
                        return
        nums.sort()
