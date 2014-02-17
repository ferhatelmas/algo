class OnTheFarmDivTwo:
    def animals(self, heads, legs):
        if legs < 2*heads or legs > 4*heads or legs%2:
            return tuple()
        x = (legs - 2*heads) / 2
        return heads-x, x
