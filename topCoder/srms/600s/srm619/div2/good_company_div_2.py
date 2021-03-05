class GoodCompanyDivTwo:
    def countGood(self, superior, workType):
        def is_diverse(d):
            w = [workType[i] for i in d]
            return len(w) == len(set(w))

        def dep(i):
            return [i] + [j for j, x in enumerate(superior) if x == i]

        return sum(is_diverse(d) for d in (dep(i) for i in xrange(len(superior))))
