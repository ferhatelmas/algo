from collections import Counter


class Solution:
    def twoSum(self, num, target):
        c = Counter(num)
        for i, a in enumerate(num, start=1):
            b = target - a
            if (a == b and c[b] > 1) or c[b] > 0:
                for j, d in enumerate(num[i:], start=i + 1):
                    if d == b:
                        return i, j
