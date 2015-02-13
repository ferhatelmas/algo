from sys import argv


with open(argv[1], 'rb') as f:
    for test in f:
        print min(
            ln.index('Y') - ln.rindex('X')
            for ln in test.rstrip().split(',')
        ) - 1
