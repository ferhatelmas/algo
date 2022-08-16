class Solution:
    def twoSum(self, num, target):
        d = {v: i for i, v in enumerate(num)}
        for i, v in enumerate(num):
            o = target - v
            if o not in d:
                continue
            if d[o] != d[v]:
                return [d[v], d[o]]
            elif i != d[o]:
                return [i, d[o]]
