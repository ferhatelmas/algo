class Solution:
    def canJump(self, nums):
        s = nums[0]
        for e in nums[1:]:
            s -= 1
            if s < 0:
                return False
            if e > s:
                s = e
        return True
