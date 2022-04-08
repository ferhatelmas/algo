class Solution:
    def summaryRanges(self, nums):
        def process(first, last):
            if first == last:
                return str(last)
            return "{}->{}".format(first, last)

        if not nums:
            return []
        p, v, r = 0, nums[0], []
        for i, e in enumerate(nums[1:], 1):
            if e - v == 1:
                v += 1
            else:
                r.append(process(nums[p], v))
                v, p = e, i
        r.append(process(nums[p], v))
        return r
