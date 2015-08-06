class Solution:
    def connect(self, root):
        h = p = None
        c = root
        while c:
            while c:
                if c.left:
                    if p:
                        p.next = c.left
                    else:
                        h = c.left
                    p = c.left
                if c.right:
                    if p:
                        p.next = c.right
                    else:
                        h = c.right
                    p = c.right
                c = c.next
            c = h
            h = p = None
