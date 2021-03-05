class EllysDirectoryListing:
    def getFiles(self, files):
        c, p, l = files.index("."), files.index(".."), len(files)
        if c + p == 2 * l - 3:
            return files
        else:
            f = list(files)
            if c < p:
                f[c], f[-1] = f[-1], f[c]
                p = f.index("..")
                f[p], f[-2] = f[-2], f[p]
            else:
                f[p], f[-1] = f[-1], f[p]
                c = f.index(".")
                f[c], f[-2] = f[-2], f[c]
            return f
