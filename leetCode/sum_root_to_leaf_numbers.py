class Solution:
    def sumNumbers(self, root):
        return self.do_sum('', root)

    def do_sum(self, v, r):
        if not r:
            return 0
        v += str(r.val)
        if not r.left and not r.right:
            return int(v)
        return self.do_sum(v, r.left) + self.do_sum(v, r.right)