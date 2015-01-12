class Solution:
    def connect(self, root):
        if root is None or root.left is None:
            return
        root.left.next = root.right
        if root.next is not None:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
