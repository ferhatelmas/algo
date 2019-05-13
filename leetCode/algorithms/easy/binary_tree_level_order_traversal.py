from itertools import izip_longest


class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        if root is None:
            return []
        return [[root.val]] + [
            a + b for a, b in izip_longest(
                self.levelOrder(root.left),
                self.levelOrder(root.right),
                fillvalue=[])
        ]
