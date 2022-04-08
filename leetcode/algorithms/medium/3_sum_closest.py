class Solution:
    def threeSumClosest(self, nums, target):
        l, m = len(nums) - 1, sum(nums[:3])
        if l < 3:
            return 0
        nums.sort()
        for i in range(l - 1):
            if i and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, l
            while j < k:
                c = sum(nums[e] for e in [i, j, k])
                if c == target:
                    return c
                if abs(target - c) < abs(target - m):
                    m = c
                if c > target:
                    k -= 1
                else:
                    j += 1
        return m
