class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = self.right = None


class Solution:
    def isSymmetric(self, root):
        def isSym(left, right):
            if left is None or right is None:
                return left == right
            if left.val != right.val:
                return False
            return isSym(left.left, right.right) and isSym(left.right, right.left)

        return isSym(root, root)
