import random


class Solution(object):
    def __init__(self, nums):
        self.original = nums[:]
        self.nums = nums

    def reset(self):
        self.nums = self.original[:]
        return self.nums

    def shuffle(self):
        random.shuffle(self.nums)
        return self.nums
