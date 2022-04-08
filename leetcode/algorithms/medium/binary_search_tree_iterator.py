class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator:
    def __init__(self, root):
        self.s = []
        c = root
        while c is not None:
            self.s.append(c)
            if c.left is not None:
                c = c.left
            else:
                break

    def hasNext(self):
        return bool(self.s)

    def next(self):
        n = c = self.s.pop()
        if c.right is not None:
            c = c.right
            while c is not None:
                self.s.append(c)
                if c.left is not None:
                    c = c.left
                else:
                    break
        return n.val
