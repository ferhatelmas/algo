from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        m, j = -1, -1
        for i, e in enumerate(nums):
            if e > m:
                m, j = e, i
        t = TreeNode(m)
        t.left = self.constructMaximumBinaryTree(nums[:j])
        t.right = self.constructMaximumBinaryTree(nums[j + 1 :])
        return t
