from typing import List


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            if num % 2 == 1:
                continue
            if num in d:
                d[num] += 1
            else:
                d[num] = 1

        mv, mn = -1, 0
        for key, value in d.items():
            if value > mn:
                mv, mn = key, value
            elif value == mn:
                if key < mv:
                    mv = key
        return mv
