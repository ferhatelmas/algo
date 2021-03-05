# Time limit
from sys import stdin

lines = stdin.readlines()
board = [[0] * 1000 for _ in xrange(1000)]

cnt = 1
for t in xrange(int(lines[0])):
    n = int(lines[cnt])

    for i in xrange(n):
        cnt += 1
        line = lines[cnt]
        for j in xrange(n):
            board[i][j] = line[j]

    cnt, boardc, w = cnt + 1, [[0] * n for _ in xrange(n)], False
    for j in xrange(n - 1, -1, -1):
        for i in xrange(n):
            c = 0
            if j + 1 < n and i - 2 >= 0:
                c = max(c, boardc[i - 2][j + 1])
            if j + 2 < n and i - 1 >= 0:
                c = max(c, boardc[i - 1][j + 2])
            if j + 1 < n and i + 2 < n:
                c = max(c, boardc[i + 2][j + 1])
            if j + 2 < n and i + 1 < n:
                c = max(c, boardc[i + 1][j + 2])

            if board[i][j] == "K":
                print c
                w = True
                break
            if board[i][j] == "P":
                c += 1
            boardc[i][j] = c

        if w:
            break
