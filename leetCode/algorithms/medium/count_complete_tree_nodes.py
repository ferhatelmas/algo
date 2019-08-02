class Solution:
    def countNodes(self, root):
        if not root:
            return 0
        leftDepth = self.getDepth(root.left)
        rightDepth = self.getDepth(root.right)
        if leftDepth == rightDepth:
            return 2 ** leftDepth + self.countNodes(root.right)
        else:
            return 2 ** rightDepth + self.countNodes(root.left)

    def getDepth(self, root):
        if not root:
            return 0
        return 1 + self.getDepth(root.left)
