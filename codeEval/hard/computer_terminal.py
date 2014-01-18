from itertools import ifilter
import re
import sys

r = c = 0
mr = mc = 10
mode = False  # overwrite
term = [' ' * mc for _ in range(mr)]


def write(s):
    global term, c
    if mode:
        term[r] = (term[r][:c] + s + term[r][c:])[:mc]
        c = min(c + len(s), mc-1)
    else:
        ls = list(term[r])
        for e in s:
            ls[c] = e
            c = min(c+1, mc-1)
        term[r] = ''.join(ls)


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    for cmd in ifilter(None, re.split(r'(\^[chbdulreio\^]|\^\d\d)', test.strip())):
        if cmd == '^c':
            term = [' ' * mc for _ in range(mr)]
        elif cmd == '^h':
            r = c = 0
        elif cmd == '^b':
            c = 0
        elif cmd == '^d':
            r = min(r+1, mr-1)
        elif cmd == '^u':
            r = max(r-1, 0)
        elif cmd == '^l':
            c = max(c-1, 0)
        elif cmd == '^r':
            c = min(c+1, mc-1)
        elif cmd == '^e':
            term[r] = term[r][:c] + ' ' * (mc-c)
        elif cmd == '^i':
            mode = True
        elif cmd == '^o':
            mode = False
        elif cmd == '^^':
            write('^')
        elif re.match(r'\^\d\d', cmd):
            r, c = map(int, cmd[1:])
        else:
            write(cmd)
test_cases.close()

print '\n'.join(term)
