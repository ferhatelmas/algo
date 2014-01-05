class ReadingBooks:
    def countBooks(self, readParts):
        c, i, l = 0, 0, len(readParts)
        while i < l-2:
            if len(set(readParts[i:i+3])) == 3:
                c += 1
                i += 3
            else:
                i += 1
        return c
