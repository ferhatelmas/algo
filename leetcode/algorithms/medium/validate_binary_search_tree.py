class Solution:
    def isValidBST(self, root):
        ls = self.inorder(root)
        for i, j in zip(ls, ls[1:]):
            if i >= j:
                return False
        return True

    def inorder(self, root):
        if root is None:
            return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)
