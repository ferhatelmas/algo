from itertools import combinations

class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        return[list(e) for i in xrange(len(S)+1) for e in combinations(sorted(S), i)]

print Solution().subsets([1, 2])


