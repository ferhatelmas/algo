from typing import List


class CustomFunction:
    # Returns f(x, y) for any given positive integers x and y.
    # Note that f(x, y) is increasing with respect to both x and y.
    # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
    def f(self, x, y):
        pass


class Solution:
    def findSolution(self, customfunction: "CustomFunction", z: int) -> List[List[int]]:
        answer, h = [], z
        for x in range(1, z + 1):
            l = 1
            while l <= h:
                y = l + (h - l) // 2
                result = customfunction.f(x, y)
                if result == z:
                    answer.append([x, y])
                    h = y - 1
                    break
                elif result < z:
                    l = y + 1
                else:
                    h = y - 1
        return answer
