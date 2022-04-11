class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        s = []

        def r(n):
            if n:
                s.append(str(n.val))
                r(n.left)
                r(n.right)
            else:
                s.append("~")

        r(root)
        return " ".join(s)

    def deserialize(self, data):
        s = iter(data.split())

        def p():
            v = next(s)
            if v == "~":
                return None
            n = TreeNode(int(v))
            n.left = p()
            n.right = p()
            return n

        return p()
