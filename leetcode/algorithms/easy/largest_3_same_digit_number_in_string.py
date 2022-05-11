class Solution:
    def largestGoodInteger(self, num: str) -> str:
        m = ""
        for i in range(len(num) - 2):
            n = num[i : i + 3]
            if len(set(n)) == 1:
                m = max(m, n)
        return m
