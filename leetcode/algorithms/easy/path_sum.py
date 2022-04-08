class Solution:
    def hasPathSum(self, root, sum):
        def hasSum(root, acc):
            if root is None:
                return False
            elif root.left is None and root.right is None:
                return acc + root.val == sum
            return hasSum(root.left, root.val + acc) or hasSum(
                root.right, root.val + acc
            )

        return hasSum(root, 0)
