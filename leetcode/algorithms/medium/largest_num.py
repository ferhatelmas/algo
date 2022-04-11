class Solution:
    def largestNumber(self, nums):
        def cmp(a, b):
            return -1 if a < b else 1

        r = sorted(map(str, nums), cmp=lambda a, b: -cmp(a + b, b + a))
        return "0" if r[0][0] == "0" else "".join(r)
