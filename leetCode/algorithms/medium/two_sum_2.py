import bisect


class Solution(object):
    def twoSum(self, numbers, target):
        l = len(numbers)
        for i, a in enumerate(numbers, start=1):
            k = target - a
            j = bisect.bisect_left(numbers, k, i)
            if j < l and numbers[j] == k:
                return [i, j + 1]
