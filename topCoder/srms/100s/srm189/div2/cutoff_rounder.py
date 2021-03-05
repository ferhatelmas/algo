class CutoffRounder:
    def round(self, num, cutoff):
        num = float(num.lstrip("0"))
        if num - int(num) >= float(cutoff):
            return int(num) + 1
        return int(num)
