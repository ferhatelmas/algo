from operator import itemgetter
from typing import Dict


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def traverse(self, root: TreeNode, level: int, cache: Dict[int, int]) -> None:
        if root is None:
            return
        cache[level] = cache.get(level, 0) + root.val
        self.traverse(root.left, level + 1, cache)
        self.traverse(root.right, level + 1, cache)

    def maxLevelSum(self, root: TreeNode) -> int:
        c = {}
        self.traverse(root, 1, c)

        return max(c.items(), key=itemgetter(1))[0]
