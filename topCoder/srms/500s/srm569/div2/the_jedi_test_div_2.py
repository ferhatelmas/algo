from math import ceil


class TheJediTestDiv2:
    def countSupervisors(self, students, Y, J):
        m, J = 50000, float(J)
        for i in xrange(len(students)):
            c = 0
            for j, v in enumerate(students):
                if i == j:
                    v -= Y
                    v = max(v, 0)
                c += int(ceil(v / J))
            m = min(m, c)
        return m
