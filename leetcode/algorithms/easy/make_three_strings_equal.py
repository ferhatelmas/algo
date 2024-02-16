from itertools import zip_longest


class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        for i, (a, b, c) in enumerate(zip_longest(s1, s2, s3)):
            if a != b or b != c:
                if i == 0:
                    return -1
                return len(s1[i:]) + len(s2[i:]) + len(s3[i:])
        return 0


print(Solution().findMinimumOperations("dac", "bac", "cac"))
