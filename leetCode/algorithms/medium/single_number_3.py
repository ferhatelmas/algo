class Solution:
    def singleNumber(self, nums):
        s = set()
        for e in nums:
            if e not in s:
                s.add(e)
            else:
                s.remove(e)
        return list(s)
