from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        answer = 0

        def dfs(node):
            if not node:
                return -1
            left = dfs(node.left)
            right = dfs(node.right)

            nonlocal answer
            answer = max(answer, left + right + 2)

            return max(left, right) + 1

        dfs(root)
        return answer
