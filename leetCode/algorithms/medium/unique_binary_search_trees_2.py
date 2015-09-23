class Solution:
    def generateTrees(self, n):
        def gen(f, s):
            t = []
            for root in range(f, s+1):
                for l in gen(f, root-1):
                    for r in gen(root+1, s):
                        node = TreeNode(root)
                        node.left = l
                        node.right = r
                        t.append(node)
            return t or [None]
        return gen(1, n)
