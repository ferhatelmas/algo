class Solution(object):
    def nextGreaterElement(self, q, nums):
        ix = {x: i for i, x in enumerate(nums)}
        return [next((y for y in nums[ix[x]+1:] if y > x), -1) for x in q]
