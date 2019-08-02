class Solution:
    def largestNumber(self, nums):
        r = sorted(map(str, nums), cmp=lambda a, b: -cmp(a + b, b + a))
        return "0" if r[0][0] == "0" else "".join(r)
