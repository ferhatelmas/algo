class SwappingDigits:
    def minNumber(self, num):
        m, l = int(num), len(num)
        for i in xrange(l):
            for j in xrange(i + 1, l):
                if (i == 0 and num[j] == "0") or num[i] < num[j]:
                    continue
                m = min(
                    m,
                    int(
                        "".join(
                            num[:i] + num[j] + num[i + 1 : j] + num[i] + num[j + 1 :]
                        )
                    ),
                )
        return m
