from collections import Counter


class Solution(object):
    def topKFrequent(self, nums, k):
        return [e for e, cnt in Counter(nums).most_common()[:k]]
