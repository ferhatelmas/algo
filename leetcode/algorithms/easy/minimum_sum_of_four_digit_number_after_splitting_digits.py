class Solution:
    def minimumSum(self, num: int) -> int:
        s = "".join(sorted(str(num)))
        n1 = int(s[0::2]) + int(s[1::2])
        n2 = int(s[:3]) + int(s[3])
        return min(n1, n2)
