class FloorLayout:
    def countBoards(self, layout):
        c = 0
        for i in xrange(len(layout)):
            for j in xrange(len(layout[i])):
                if j > 0 and layout[i][j] == '-' and layout[i][j-1] == '-':
                    continue
                if i > 0 and layout[i][j] == '|' and layout[i-1][j] == '|':
                    continue
                c += 1
        return c
