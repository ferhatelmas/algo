class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def depth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1

    def leaveSum(self, root: TreeNode, level: int, max_level: int) -> int:
        if root is None:
            return 0
        level += 1
        if root.left is None and root.right is None and level == max_level:
            return root.val
        return self.leaveSum(root.left, level, max_level) + self.leaveSum(
            root.right, level, max_level
        )

    def deepestLeavesSum(self, root: TreeNode) -> int:
        return self.leaveSum(root, 0, self.depth(root))
