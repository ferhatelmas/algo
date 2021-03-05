class AccessChanger:
    def convert(self, program):
        r = []
        for l in program:
            i = l.find("//")
            if i == -1:
                r.append(l.replace("->", "."))
            else:
                r.append(l[:i].replace("->", ".") + l[i:])
        return r
