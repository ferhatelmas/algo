from string import ascii_uppercase

class AlphabetPath:
    def doesItExist(self, letterMaze):
        pi, pj = -1, -1
        for e in ascii_uppercase:
            for i, x in enumerate(letterMaze):
                for j, y in enumerate(x):
                    if y == e:
                        if e != 'A' and abs(i-pi) + abs(j-pj) != 1:
                            return 'NO'
                        pi, pj = i, j
        return 'YES'
