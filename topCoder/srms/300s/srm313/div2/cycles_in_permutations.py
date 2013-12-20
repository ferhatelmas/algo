class CyclesInPermutations:
    def maxCycle(self, board):
        def cycle(i):
            c, n = 1, board[i]
            while n != i + 1:
                c += 1
                n = board[n - 1]
            return c
        return max(map(cycle, xrange(len(board))))
