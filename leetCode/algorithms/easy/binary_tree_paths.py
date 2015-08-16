class Solution:
    def binaryTreePaths(self, root):
        def s(r, p, res):
            if not r.left and not r.right:
                res.append(p)
                return
            if r.left:
                s(r.left, p + "->" + str(r.left.val), res)
            if r.right:
                s(r.right, p + "->" + str(r.right.val), res)
        ls = []
        if root:
            s(root, str(root.val), ls)
        return ls
