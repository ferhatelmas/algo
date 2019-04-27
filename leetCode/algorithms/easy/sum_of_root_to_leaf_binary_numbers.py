class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sum(self, node: TreeNode, num: str) -> int:
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return int(num+str(node.val), 2)
        num += str(node.val)
        return self.sum(node.left, num) + self.sum(node.right, num)

    def sumRootToLeaf(self, root: TreeNode) -> int:
        return self.sum(root, '')
