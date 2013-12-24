class AttendanceShort:
    def shortList(self, names, attendance):
        def is_fine(a):
            return float(a.count('P')) / (a.count('A') + a.count('P')) >= 0.75
        return [n for n, a in zip(names, attendance) if not is_fine(a)]
