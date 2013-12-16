import re

class RunLengthEncoding:
    def decode(self, text):
        s = ''
        for m in re.findall('(\d*\w)', text):
            l = len(m)
            if l == 1:
                c = 1
            elif l > 3:
                return 'TOO LONG'
            else:
                c = int(m[:-1])
            s += (c * m[-1])
        return 'TOO LONG' if len(s) > 50 else s
