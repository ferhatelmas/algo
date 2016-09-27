import random


class Solution(object):
    def __init__(self, nums):
        self.nums = nums

    def pick(self, target):
        r, c = -1, 0
        for i, e in enumerate(self.nums):
            if e == target:
                if random.randint(0, c) == 0:
                    r = i
                c += 1
        return r
