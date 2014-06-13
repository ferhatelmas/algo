import colorsys as c
import sys

def cmyk_to_rgb(*args):
    return (255 * (1-e) * (1-args[-1]) for e in args[:-1])

def get_params(line):
    return [e/(100.0 if i else 360.0)
            for i, e in enumerate(float(n)
            for n in line[4:-2].split(','))]

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if test.startswith('HSL'):
        res = (255*e for e in c.hls_to_rgb(*get_params(test)))
    elif test.startswith('HSV'):
        res = (255*e for e in c.hsv_to_rgb(*get_params(test)))
    elif test.startswith('#'):
        res = (int(test[i:i+2], 16) for i in (1, 3, 5))
    else:
        res = cmyk_to_rgb(*(float(n) for n in test[1:-2].split(',')))
    print 'RGB({},{},{})'.format(*(int(round(e)) for e in res))

test_cases.close()
