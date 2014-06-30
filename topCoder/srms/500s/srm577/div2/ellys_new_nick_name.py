class EllysNewNickname:
    def getLength(self, nickname):
        c, v = 0, 0
        for e in nickname:
            if e in 'aeiouy':
                v += 1
            else:
                if v:
                    c += 1
                    v = 0
                c += 1
        return c + min(v, 1)
