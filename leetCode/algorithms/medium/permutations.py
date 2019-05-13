from itertools import permutations


class Solution:
    def permute(self, num):
        return [list(l) for l in permutations(num)]
