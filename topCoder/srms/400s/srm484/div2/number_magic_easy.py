class NumberMagicEasy:
    def theNumber(self, answer):
        s1 = set([1,2,3,4,5,6,7,8])
        s2 = set([1,2,3,4,9,10,11,12])
        s3 = set([1,2,5,6,9,10,13,14])
        s4 = set([1,3,5,7,9,11,13,15])
        s = set(range(1, 17))
        for i, e in enumerate(answer, 1):
            o = eval('s' + str(i))
            if e == 'Y':
                s &= o
            else:
                s -= o
        return s.pop()
