class Solution:
    def pathSum(self, root, sum):
        res = []
        self.findPaths(root, sum, [], res)
        return res

    def findPaths(self, root, sum, p, res):
        if root is None:
            return
        p.append(root.val)
        if root.left is None and root.right is None and sum == root.val:
            res.append([e for e in p])
        self.findPaths(root.left, sum - root.val, p, res)
        self.findPaths(root.right, sum - root.val, p, res)
        p.pop()
