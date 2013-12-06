class bloggoShortcuts:
    def expand(self, text):
        b, i, r = False, False, []
        for e in text:
            if e == '_':
                r.append('</i>' if i else '<i>')
                i = not i
            elif e == '*':
                r.append('</b>' if b else '<b>')
                b = not b
            else:
                r.append(e)
        return ''.join(r)
