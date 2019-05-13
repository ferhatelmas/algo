class Solution:
    def containsNearbyDuplicate(self, nums, k):
        if k == 0:
            return False
        s = set(nums[:k + 1])
        if len(s) < len(nums[:k + 1]):
            return True
        for i, e in enumerate(nums[k + 1:]):
            s.remove(nums[i])
            if e in s:
                return True
            s.add(e)
        return False
