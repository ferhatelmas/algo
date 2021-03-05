class Birthday:
    def getNext(self, date, birthdays):
        def c(e):
            return e.split()[0]

        ls = sorted(birthdays)
        for b in ls:
            if b >= date:
                return c(b)
        return c(ls[0])
