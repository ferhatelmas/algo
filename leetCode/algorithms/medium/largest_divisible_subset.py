class Solution:
    def largestDivisibleSubset(self, nums):
        size, last, l = 0, 0, len(nums)
        sizes, prev = [0] * l, [0] * l
        nums.sort()
        for i in range(l - 1, -1, -1):
            for j, f in enumerate(nums[i:], start=i):
                if f % nums[i] == 0 and sizes[i] < 1 + sizes[j]:
                    sizes[i], prev[i] = 1 + sizes[j], j
                    if sizes[i] > size:
                        size, last = sizes[i], i
        ls = []
        for _ in range(size):
            ls.append(nums[last])
            last = prev[last]
        return ls
