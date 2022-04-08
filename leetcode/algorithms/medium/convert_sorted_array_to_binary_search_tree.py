class Solution:
    def sortedArrayToBST(self, num):
        if not num:
            return None
        l = len(num)
        if l == 1:
            return TreeNode(num[0])
        t = TreeNode(num[l / 2])
        t.left = self.sortedArrayToBST(num[: l / 2])
        t.right = self.sortedArrayToBST(num[l / 2 + 1 :])
        return t
