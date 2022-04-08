from collections import Counter


class Solution(object):
    def findRestaurant(self, l1, l2):
        common = set(l1) & set(l2)
        counts = Counter({k: i for i, k in enumerate(l1) if k in common})
        counts.update({k: i for i, k in enumerate(l2) if k in common})
        m = min(counts.values())
        return [k for k, v in counts.items() if v == m]
