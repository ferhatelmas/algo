class Solution:

    def majorityElement(self, num):
        return sorted(num)[len(num) / 2]
