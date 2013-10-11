import sys

def separate(ls):
    ns, ss = [], []
    for e in ls:
        try:
            int(e)
            ns.append(e)
        except:
            ss.append(e)
    if ns and ss:
        return '%s|%s' % (','.join(ss), ','.join(ns))

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    res = separate(test.strip().split(','))
    print res if res else test.strip()
test_cases.close()
