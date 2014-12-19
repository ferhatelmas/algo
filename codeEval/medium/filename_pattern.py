import re
import sys


with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        files = test.rstrip().split()
        p = re.compile(files[0].replace('.', '\.')
                       .replace('*', '.*')
                       .replace('?', '.') + '$')
        r = ' '.join(f for f in files[1:] if re.match(p, f))
        print r if r else '-'
