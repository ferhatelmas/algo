import operator


class Solution(object):
    def findRelativeRanks(self, nums):
        ls = sorted(enumerate(nums), key=operator.itemgetter(1), reverse=True)
        res = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                v = "Gold Medal"
            elif i == 1:
                v = "Silver Medal"
            elif i == 2:
                v = "Bronze Medal"
            else:
                v = str(i+1)
            res[ls[i][0]] = v
        return res
