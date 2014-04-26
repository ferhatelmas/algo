class NetworkXZeroOne:
    def reconstruct(self, message):
        for e in 'xo':
            s = list(message)
            for i, w in enumerate(s):
                if w == '?':
                    s[i] = e
                elif w != e:
                    break
                e = 'o' if e == 'x' else 'x'
            else:
                return ''.join(s)
