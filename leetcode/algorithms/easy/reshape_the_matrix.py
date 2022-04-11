import itertools


class Solution(object):
    def matrixReshape(self, nums, r, c):
        l = len(nums) * len(nums[0])
        if l != r * c:
            return nums
        it = itertools.chain(*nums)
        return [list(itertools.islice(it, 0, c)) for i in range(0, l, c)]
