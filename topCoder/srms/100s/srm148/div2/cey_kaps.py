class CeyKaps:
    def decipher(self, typed, switches):
        ss = []
        for e in typed:
            for s in switches:
                if s[0] == e:
                    e = s[2]
                elif s[2] == e:
                    e = s[0]
            ss.append(e)
        return ''.join(ss)
