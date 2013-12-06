class TitleString:
    def toFirstUpperCase(self, title):
        return ''.join(map(
            lambda (i, e): e.upper() if 'a' <= e <= 'z' and (not ('a' <= title[i-1] <= 'z') or i == 0) else e,
            enumerate(title)
        ))
