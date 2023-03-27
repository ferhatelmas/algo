class Solution:
    def kItemsWithMaximumSum(
        self, numOnes: int, numZeros: int, numNegOnes: int, k: int
    ) -> int:
        s = numOnes + numZeros
        if k <= s:
            return min(numOnes, k)
        return numOnes - k + s
