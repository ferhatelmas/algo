class Containers:
    def wastedSpace(self, containers, packages):
        i, j, s, l, c = 0, 0, 0, len(packages), containers[0]
        while j < l:
            if c < packages[j]:
                s += c
                i += 1
                c = containers[i]
            else:
                c -= packages[j]
                j += 1
        return s + c + sum(containers[i+1:])
