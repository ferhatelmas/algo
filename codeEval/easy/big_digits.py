import sys

digits = """-**----*--***--***---*---****--**--****--**---**--
*--*--**-----*----*-*--*-*----*-------*-*--*-*--*-
*--*---*---**---**--****-***--***----*---**---***-
*--*---*--*-------*----*----*-*--*--*---*--*----*-
-**---***-****-***-----*-***---**---*----**---**--
--------------------------------------------------"""

big_digits = zip(*[[e[i:i+5] for i in xrange(0, len(e), 5)] for e in digits.split()])

def magnify(s):
    return "\n".join(("".join(ln) for ln in zip(*(big_digits[int(e)] for e in s if '0' <= e <= '9'))))

f = open(sys.argv[1], 'r')
for test in f:
    print magnify(test.rstrip())
f.close()
