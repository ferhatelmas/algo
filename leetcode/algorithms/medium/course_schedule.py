class Solution:
    def canFinish(self, n, pre):
        if n <= 0:
            return False
        ind = [0] * n
        for a, b in pre:
            ind[b] += 1
        q = [i for i, e in enumerate(ind) if e == 0]
        while q:
            x, q = q[0], q[1:]
            for a, b in pre:
                if x == a:
                    ind[b] -= 1
                    if ind[b] == 0:
                        q.append(b)
        return not any(ind)
