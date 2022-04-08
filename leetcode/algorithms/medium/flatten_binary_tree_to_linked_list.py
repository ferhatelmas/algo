class Solution:
    def flatten(self, root):
        if not root:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        t = root.right
        root.right = root.left
        root.left = None
        while root.right:
            root = root.right
        root.right = t
