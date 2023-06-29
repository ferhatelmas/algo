from typing import List


class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        l, ls = len(nums), []
        for i in range(l):
            ls.append(nums[i][i])
            ls.append(nums[i][l - i - 1])
        ls.sort(reverse=True)

        sieve, m = set(), max(ls)
        for i in range(2, m + 1):
            if i in sieve:
                continue
            for j in range(i * 2, m + 1, i):
                sieve.add(j)
        for i in ls:
            if i != 1 and i not in sieve:
                return i
        return 0
