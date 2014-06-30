from itertools import groupby

class FoxAndGomoku:
    def win(self, board):
        def b(s):
            return any(k == 'o' and len(list(g)) >= 5 for k, g in groupby(s))

        for r in board:
            if b(r):
                return 'found'

        for c in zip(*board):
            if b(c):
                return 'found'


        rr, rc = len(board), len(board[0])
        for i in xrange(rr):
            s = ''.join([board[i+j][j] for j in xrange(min(rr-i, rc))])
            r = ''.join([board[i+j][rc-j-1] for j in xrange(min(rr-i, rc))])
            if b(s) or b(r):
                return 'found'

        for i in xrange(rc):
            s = ''.join([board[j][i+j] for j in xrange(min(rr, rc-i))])
            r = ''.join([board[j][i-j] for j in xrange(min(rr, i+1))])
            if b(s) or b(r):
                return 'found'

        return 'not found'
