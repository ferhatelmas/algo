class Solution:
    def invertTree(self, root):
        if not root:
            return root
        l = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(l)
        return root
